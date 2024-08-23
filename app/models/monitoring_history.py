from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class MonitoringHistory(Base):
    __tablename__ = 'monitoring_history'

    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey('instagram_profiles.id'), nullable=False)
    action = Column(String(255), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())