from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash, verify_password
from fastapi import HTTPException, status

# User operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# Trip operations
def get_trips(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Trip).filter(models.Trip.user_id == user_id).offset(skip).limit(limit).all()

def get_trip(db: Session, trip_id: int, user_id: int):
    return db.query(models.Trip).filter(models.Trip.id == trip_id, models.Trip.user_id == user_id).first()

def create_trip(db: Session, trip: schemas.TripCreate, user_id: int):
    db_trip = models.Trip(**trip.model_dump(), user_id=user_id)
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

def update_trip(db: Session, trip_id: int, trip: schemas.TripCreate, user_id: int):
    db_trip = get_trip(db, trip_id, user_id)
    if db_trip is None:
        return None
    
    update_data = trip.model_dump()
    for key, value in update_data.items():
        setattr(db_trip, key, value)
    
    db.commit()
    db.refresh(db_trip)
    return db_trip

def delete_trip(db: Session, trip_id: int, user_id: int):
    db_trip = get_trip(db, trip_id, user_id)
    if db_trip is None:
        return None
    
    db.delete(db_trip)
    db.commit()
    return db_trip

# Note operations
def get_notes(db: Session, trip_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Note).filter(models.Note.trip_id == trip_id).offset(skip).limit(limit).all()

def get_note(db: Session, note_id: int, trip_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id, models.Note.trip_id == trip_id).first()

def create_note(db: Session, note: schemas.NoteCreate, trip_id: int):
    db_note = models.Note(**note.model_dump(), trip_id=trip_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def update_note(db: Session, note_id: int, note: schemas.NoteCreate, trip_id: int):
    db_note = get_note(db, note_id, trip_id)
    if db_note is None:
        return None
    
    update_data = note.model_dump()
    for key, value in update_data.items():
        setattr(db_note, key, value)
    
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int, trip_id: int):
    db_note = get_note(db, note_id, trip_id)
    if db_note is None:
        return None
    
    db.delete(db_note)
    db.commit()
    return db_note