from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.profile_repository import ProfileRepository
from app.database import SessionLocal
from app.schemas.profile_schema import ProfileCreate, ProfileResponse, MonitoringHistoryResponse
from app.controllers.auth_controller import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/profiles/", response_model=ProfileResponse)
def create_profile(profile_create: ProfileCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    profile_repo = ProfileRepository(db)
    return profile_repo.create_profile(handle=profile_create.handle, bio_text=profile_create.bio_text, user_id=current_user.id)

@router.get("/profiles/", response_model=list[ProfileResponse])
def list_profiles(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    profile_repo = ProfileRepository(db)
    return profile_repo.get_profiles_by_user(user_id=current_user.id)

@router.post("/profiles/{profile_id}/monitor", response_model=MonitoringHistoryResponse)
def monitor_profile(profile_id: int, action: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    profile_repo = ProfileRepository(db)
    profile = profile_repo.get_profiles_by_user(user_id=current_user.id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return profile_repo.log_monitoring_action(profile_id=profile_id, action=action)