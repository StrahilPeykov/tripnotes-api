from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import date, datetime

# User base schemas (without trips relationship)
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True  

# Trip schemas
class TripBase(BaseModel):
    title: str
    destination: str
    date: date

class TripCreate(TripBase):
    pass

# Note schemas
class NoteBase(BaseModel):
    content: str

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    created_at: datetime
    trip_id: int

    class Config:
        from_attributes = True  

class Trip(TripBase):
    id: int
    created_at: datetime
    user_id: int
    notes: List[Note] = []

    class Config:
        from_attributes = True 

# Complete User schema with trips (defined after Trip)
class User(UserInDB):
    trips: List[Trip] = []

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None