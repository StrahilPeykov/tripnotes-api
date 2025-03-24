from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import date, datetime

# User schemas
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class User(UserInDB):
    pass

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None