from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class ProgressMetric(Base):
    __tablename__ = "progress_metrics"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    metric_type = Column(String(50), nullable=False)  # e.g., weight, body_fat, muscle_mass
    value = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False)  # date of measurement
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="progress_metrics")