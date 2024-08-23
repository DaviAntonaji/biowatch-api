import sys
import os
import instaloader
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.instagram_profile import InstagramProfile
from app.models.monitoring_history import MonitoringHistory
from datetime import datetime

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_bio_for_text(profile: InstagramProfile, db: Session):
    loader = instaloader.Instaloader()

    try:
        ig_profile = instaloader.Profile.from_username(loader.context, profile.handle)

        # Verifica se o texto está na bio do perfil
        text_in_bio = profile.bio_text in ig_profile.biography

        # Obtém o último registro de histórico para esse perfil
        last_history = db.query(MonitoringHistory).filter_by(profile_id=profile.id).order_by(MonitoringHistory.timestamp.desc()).first()

        if last_history is None:
            # Nenhum histórico encontrado, cria o primeiro registro
            action = "Texto presente" if text_in_bio else "Texto ausente"
            log_monitoring_action(profile.id, action, db)
        else:
            # Verifica se o status mudou em relação ao último histórico
            if last_history.action == "Texto presente" and not text_in_bio:
                log_monitoring_action(profile.id, "Texto ausente", db)
            elif last_history.action == "Texto ausente" and text_in_bio:
                log_monitoring_action(profile.id, "Texto presente", db)

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"O perfil {profile.handle} não foi encontrado. Verifique se o nome de usuário está correto.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def log_monitoring_action(profile_id: int, action: str, db: Session):
    history = MonitoringHistory(profile_id=profile_id, action=action, timestamp=datetime.utcnow())
    db.add(history)
    db.commit()
    print(f"Histórico de monitoramento atualizado: {action}")

def run_worker():
    db = SessionLocal()
    try:
        profiles = db.query(InstagramProfile).all()
        for profile in profiles:
            check_bio_for_text(profile, db)
    finally:
        db.close()

if __name__ == "__main__":
    run_worker()