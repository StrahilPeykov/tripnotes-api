from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, List
from datetime import date, datetime

# User schemas
class UserBase(BaseModel):
    email: EmailStr = Field(description="User's email address")

class UserCreate(UserBase):
    password: str = Field(min_length=8, description="User's password (min 8 characters)")

    @field_validator('password')
    @classmethod
    def password_complexity(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        return v

# Trip schemas
class TripBase(BaseModel):
    title: str = Field(min_length=3, max_length=100, description="Trip title")
    destination: str = Field(min_length=3, max_length=100, description="Trip destination")
    trip_date: date = Field(description="Trip date") 

    @field_validator('trip_date')
    @classmethod
    def validate_trip_date(cls, v):
        if v < date.today():
            raise ValueError('Trip date cannot be in the past')
        return v

# Note schemas
class NoteBase(BaseModel):
    content: str = Field(min_length=1, description="Note content")
    media_url: Optional[str] = Field(default=None, description="Optional URL to media")

    @field_validator('media_url')
    @classmethod
    def validate_url(cls, v):
        if v is not None and not v.startswith(('http://', 'https://')):
            raise ValueError('Media URL must be a valid HTTP or HTTPS URL')
        return v

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    created_at: datetime
    trip_id: int

    class Config:
        from_attributes = True

class TripCreate(TripBase):
    pass

class Trip(TripBase):
    id: int
    created_at: datetime
    user_id: int
    notes: List[Note] = []

    class Config:
        from_attributes = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# User schema to include trips
class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class User(UserInDB):
    trips: List[Trip] = []