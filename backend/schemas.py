from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

# --- ENUMS ---
# We redefine these as string Enums so FastAPI knows how to read them from JSON
class RoleEnum(str, Enum):
    student = "student"
    admin = "admin"

class MealTypeEnum(str, Enum):
    breakfast = "breakfast"
    lunch = "lunch"
    dinner = "dinner"

class TokenStatusEnum(str, Enum):
    active = "active"
    scanned = "scanned"
    cancelled = "cancelled"


# --- USER SCHEMAS ---
class UserBase(BaseModel):
    name: str
    roll_number: str
    role: RoleEnum = RoleEnum.student

# Used when a user is signing up (Requires a password)
class UserCreate(UserBase):
    password: str

# Used when sending user data back to the frontend (Hides the password!)
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


# --- MEAL SCHEMAS ---
class MealBase(BaseModel):
    meal_type: MealTypeEnum
    description: str
    is_active: bool = True

class MealCreate(MealBase):
    pass

class MealResponse(MealBase):
    id: int
    date: datetime

    class Config:
        from_attributes = True


# --- TOKEN SCHEMAS ---
class TokenBase(BaseModel):
    meal_id: int

class TokenCreate(TokenBase):
    user_id: int

class TokenResponse(TokenBase):
    id: str  # This is the UUID that will become our QR Code
    user_id: int
    status: TokenStatusEnum
    created_at: datetime
    scanned_at: Optional[datetime] = None

    class Config:
        from_attributes = True