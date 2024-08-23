from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class InstagramProfile(Base):
    __tablename__ = 'instagram_profiles'

    id = Column(Integer, primary_key=True, index=True)
    handle = Column(String(255), nullable=False)
    bio_text = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Importação tardia da classe User
    @property
    def user(self):
        from app.models.user_model import User
        return relationship(User)