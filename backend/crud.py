from sqlalchemy.orm import Session
from datetime import datetime
import models, schemas

# --- USERS ---
def get_user_by_roll_number(db: Session, roll_number: str):
    """Finds a user by their roll number (used for logging in)."""
    return db.query(models.User).filter(models.User.roll_number == roll_number).first()

def create_user(db: Session, user: schemas.UserCreate):
    """Saves a new user to the database."""
    # Note: In a production app, you MUST securely hash the password using a library like passlib.
    # For this project setup, we are doing a simplified hash simulation.
    fake_hashed_password = user.password + "_hashed" 
    
    db_user = models.User(
        name=user.name, 
        roll_number=user.roll_number, 
        password_hash=fake_hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- MEALS ---
def create_meal(db: Session, meal: schemas.MealCreate):
    """Allows an admin to add a new meal to the menu."""
    db_meal = models.Meal(**meal.model_dump())
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

def get_active_meals(db: Session):
    """Fetches all meals that are currently active so students can view them."""
    return db.query(models.Meal).filter(models.Meal.is_active == True).all()

# --- TOKENS ---
def create_token(db: Session, token: schemas.TokenCreate):
    """Generates a token, preventing double-booking."""
    # 1. Check if the user already booked this exact meal
    existing_token = db.query(models.Token).filter(
        models.Token.user_id == token.user_id,
        models.Token.meal_id == token.meal_id,
        models.Token.status != models.TokenStatusEnum.cancelled
    ).first()
    
    if existing_token:
        return None  # We will tell the API to return a 400 Error if this happens

    # 2. Create and save the new token
    db_token = models.Token(user_id=token.user_id, meal_id=token.meal_id)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def scan_token(db: Session, token_id: str):
    """Marks a token as scanned by an admin."""
    db_token = db.query(models.Token).filter(models.Token.id == token_id).first()
    
    # If the QR code is fake or doesn't exist
    if not db_token:
        return None
        
    # If the student tries to show a screenshot of an already used QR code
    if db_token.status == models.TokenStatusEnum.scanned:
        return "ALREADY_SCANNED"
        
    # Success: Mark it as scanned
    db_token.status = models.TokenStatusEnum.scanned
    db_token.scanned_at = datetime.utcnow()
    db.commit()
    db.refresh(db_token)
    return db_token