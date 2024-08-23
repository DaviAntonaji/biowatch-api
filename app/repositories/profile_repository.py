from sqlalchemy.orm import Session
from app.models.instagram_profile import InstagramProfile
from app.models.monitoring_history import MonitoringHistory

class ProfileRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_profile(self, handle: str, bio_text: str, user_id: int):
        profile = InstagramProfile(handle=handle, bio_text=bio_text, user_id=user_id)
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile

    def get_profiles_by_user(self, user_id: int):
        return self.db.query(InstagramProfile).filter(InstagramProfile.user_id == user_id).all()

    def log_monitoring_action(self, profile_id: int, action: str):
        history = MonitoringHistory(profile_id=profile_id, action=action)
        self.db.add(history)
        self.db.commit()
        self.db.refresh(history)
        return history