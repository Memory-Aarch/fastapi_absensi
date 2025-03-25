from pydantic import BaseModel, EmailStr
from datetime import datetime

# Schema untuk registrasi user
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Schema untuk login user
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema untuk response user tanpa password
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # Konversi dari SQLAlchemy model

# Schema untuk token response
class Token(BaseModel):
    access_token: str
    token_type: str

# Schema untuk request absen (check-in/check-out)
class AttendanceCreate(BaseModel):
    status: str  # "check-in" atau "check-out"

# Schema untuk response absen
class AttendanceResponse(BaseModel):
    id: int
    user_id: int
    status: str
    timestamp: datetime

    class Config:
        from_attributes = True
