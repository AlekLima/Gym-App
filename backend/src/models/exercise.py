from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)
    muscle_group = Column(String(50), nullable=True, index=True)
    equipment_needed = Column(String(100), nullable=True)