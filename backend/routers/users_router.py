from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, crud, database

router = APIRouter(prefix="/api/users", tags=["Users"])

# Dependency to get the database session per request
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Registers a new student or admin in the system."""
    db_user = crud.get_user_by_roll_number(db, roll_number=user.roll_number)
    if db_user:
        raise HTTPException(
            status_code=400, 
            detail="A user with this roll number already exists."
        )
    return crud.create_user(db=db, user=user)