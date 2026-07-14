from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.core.database import Base

class Set(Base):
    __tablename__ = "sets"

    id = Column(Integer, primary_key=True, index=True)
    workout_session_id = Column(Integer, ForeignKey("workout_sessions.id"))
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)  # in kg or lbs
    order = Column(Integer, nullable=False)  # order of the set in the workout

    # Relationships
    workout_session = relationship("WorkoutSession", back_populates="sets")
    exercise = relationship("Exercise")