from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    trips = relationship("Trip", back_populates="owner", cascade="all, delete-orphan")

class Trip(Base):
    __tablename__ = "trips"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    destination = Column(String, index=True)
    date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="trips")
    notes = relationship("Note", back_populates="trip", cascade="all, delete-orphan")

class Note(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    media_url = Column(String, nullable=True)  # Optional field for image links
    trip_id = Column(Integer, ForeignKey("trips.id"))
    
    trip = relationship("Trip", back_populates="notes")