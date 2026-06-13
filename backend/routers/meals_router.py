from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
import schemas, crud, database

router = APIRouter(prefix="/api/meals", tags=["Meals"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MealResponse, status_code=status.HTTP_201_CREATED)
def add_meal(meal: schemas.MealCreate, db: Session = Depends(get_db)):
    """Allows admins to insert a new meal into the schedule."""
    return crud.create_meal(db=db, meal=meal)

@router.get("/", response_model=List[schemas.MealResponse])
def view_menu(db: Session = Depends(get_db)):
    """Allows students to view all active meals on the menu."""
    return crud.get_active_meals(db=db)