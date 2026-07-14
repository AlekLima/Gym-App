from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.WorkoutRoutine])
def read_workout_routines(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Retrieve workout routines.
    """
    workout_routines = crud.workout_routine.get_multi_by_owner(
        db, owner_id=current_user.id, skip=skip, limit=limit
    )
    return workout_routines

@router.post("/", response_model=schemas.WorkoutRoutine)
def create_workout_routine(
    *,
    db: Session = Depends(deps.get_db),
    workout_routine_in: schemas.WorkoutRoutineCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Create new workout routine.
    """
    workout_routine = crud.workout_routine.create_with_owner(
        db, obj_in=workout_routine_in, owner_id=current_user.id
    )
    return workout_routine

@router.put("/{id}", response_model=schemas.WorkoutRoutine)
def update_workout_routine(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    workout_routine_in: schemas.WorkoutRoutineUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Update a workout routine.
    """
    workout_routine = crud.workout_routine.get(db=db, id=id)
    if not workout_routine:
        raise HTTPException(status_code=404, detail="Workout routine not found")
    if workout_routine.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    workout_routine = crud.workout_routine.update(
        db, db_obj=workout_routine, obj_in=workout_routine_in
    )
    return workout_routine

@router.get("/{id}", response_model=schemas.WorkoutRoutine)
def read_workout_routine(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Get workout routine by ID.
    """
    workout_routine = crud.workout_routine.get(db=db, id=id)
    if not workout_routine:
        raise HTTPException(status_code=404, detail="Workout routine not found")
    if workout_routine.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return workout_routine

@router.delete("/{id}", response_model=schemas.WorkoutRoutine)
def delete_workout_routine(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Delete a workout routine.
    """
    workout_routine = crud.workout_routine.get(db=db, id=id)
    if not workout_routine:
        raise HTTPException(status_code=404, detail="Workout routine not found")
    if workout_routine.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    workout_routine = crud.workout_routine.remove(db=db, id=id)
    return workout_routine