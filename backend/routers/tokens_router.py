from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, crud, database

router = APIRouter(prefix="/api/tokens", tags=["Tokens"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TokenResponse, status_code=status.HTTP_201_CREATED)
def book_token(token: schemas.TokenCreate, db: Session = Depends(get_db)):
    """Generates a token for a student. Prevents double booking."""
    new_token = crud.create_token(db=db, token=token)
    if not new_token:
        raise HTTPException(
            status_code=400, 
            detail="You have already booked a token for this meal!"
        )
    return new_token

@router.put("/{token_id}/scan", response_model=schemas.TokenResponse)
def validate_and_scan_token(token_id: str, db: Session = Depends(get_db)):
    """Called when an admin scans a student's QR code."""
    result = crud.scan_token(db=db, token_id=token_id)
    
    if result is None:
        raise HTTPException(status_code=404, detail="Invalid Token or Fake QR Code!")
        
    if result == "ALREADY_SCANNED":
        raise HTTPException(status_code=400, detail="Warning: This token has already been used!")
        
    return result