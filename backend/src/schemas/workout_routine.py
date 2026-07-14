from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WorkoutRoutineBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_public: bool = False

class WorkoutRoutineCreate(WorkoutRoutineBase):
    pass

class WorkoutRoutineUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_public: Optional[bool] = None

class WorkoutRoutineInDBBase(WorkoutRoutineBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class WorkoutRoutine(WorkoutRoutineInDBBase):
    pass

class WorkoutRoutineInDB(WorkoutRoutineInDBBase):
    pass