from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict
from app.models.user import UserRole


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    role: UserRole
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)