from pydantic import BaseModel
from datetime import datetime

class ProfileBase(BaseModel):
    handle: str
    bio_text: str

class ProfileCreate(ProfileBase):
    pass


class ProfileResponse(BaseModel):
    id: int
    handle: str
    bio_text: str
    user_id: int
    created_at: datetime
    updated_at: datetime | None

    class Config:
        orm_mode = True

class MonitoringHistoryResponse(BaseModel):
    id: int
    profile_id: int
    action: str
    timestamp: str

    class Config:
        ...