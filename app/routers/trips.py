from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, crud, models, auth
from ..database import get_db

router = APIRouter(
    prefix="/trips",
    tags=["trips"],
    dependencies=[Depends(auth.get_current_active_user)]
)

@router.get("/", response_model=List[schemas.Trip])
def read_trips(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    """
    Get all trips for the current user.
    """
    trips = crud.get_trips(db, user_id=current_user.id, skip=skip, limit=limit)
    return trips

@router.post("/", response_model=schemas.Trip, status_code=status.HTTP_201_CREATED)
def create_trip(
    trip: schemas.TripCreate, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    """
    Create a new trip for the current user.
    """
    return crud.create_trip(db=db, trip=trip, user_id=current_user.id)

@router.get("/{trip_id}", response_model=schemas.Trip)
def read_trip(
    trip_id: int, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    """
    Get a specific trip by ID.
    """
    db_trip = crud.get_trip(db, trip_id=trip_id, user_id=current_user.id)
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return db_trip

@router.put("/{trip_id}", response_model=schemas.Trip)
def update_trip(
    trip_id: int, 
    trip: schemas.TripCreate, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    """
    Update a trip by ID.
    """
    db_trip = crud.update_trip(db, trip_id=trip_id, trip=trip, user_id=current_user.id)
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return db_trip

@router.delete("/{trip_id}", response_model=schemas.Trip)
def delete_trip(
    trip_id: int, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_active_user)
):
    """
    Delete a trip by ID.
    """
    db_trip = crud.delete_trip(db, trip_id=trip_id, user_id=current_user.id)
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return db_trip