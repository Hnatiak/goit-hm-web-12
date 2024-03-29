from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import date

class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    # last_name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=10, max_length=50)

class UserResponse(BaseModel):
    id: int = 1
    username: str
    email: EmailStr
    avatar: str

    class Config:
        from_attributes = True

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"