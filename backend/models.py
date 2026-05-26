from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
import enum
from datetime import datetime
import uuid
from database import Base

# --- ENUMS (Allowed values for specific columns) ---
class RoleEnum(enum.Enum):
    student = "student"
    admin = "admin"

class MealTypeEnum(enum.Enum):
    breakfast = "breakfast"
    lunch = "lunch"
    dinner = "dinner"

class TokenStatusEnum(enum.Enum):
    active = "active"
    scanned = "scanned"
    cancelled = "cancelled"

# --- DATABASE TABLES ---
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    roll_number = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.student)

    # Relationships
    tokens = relationship("Token", back_populates="owner")

class Meal(Base):
    __tablename__ = "meals"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    meal_type = Column(Enum(MealTypeEnum))
    description = Column(String)
    is_active = Column(Boolean, default=True)

    # Relationships
    tokens = relationship("Token", back_populates="meal")

class Token(Base):
    __tablename__ = "tokens"
    
    # We use a UUID here so the QR code contains a secure, unguessable string
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    meal_id = Column(Integer, ForeignKey("meals.id"))
    status = Column(Enum(TokenStatusEnum), default=TokenStatusEnum.active)
    created_at = Column(DateTime, default=datetime.utcnow)
    scanned_at = Column(DateTime, nullable=True)

    # Relationships
    owner = relationship("User", back_populates="tokens")
    meal = relationship("Meal", back_populates="tokens")