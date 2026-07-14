from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class WorkoutSession(Base):
    __tablename__ = "workout_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    workout_routine_id = Column(Integer, ForeignKey("workout_routines.id"), nullable=True)
    date = Column(DateTime, default=datetime.utcnow)
    duration = Column(Integer, nullable=True)  # in minutes
    notes = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

    # Relationships
    user = relationship("User", back_populates="workout_sessions")
    workout_routine = relationship("WorkoutRoutine", back_populates="workout_sessions")
    sets = relationship("Set", back_populates="workout_session")