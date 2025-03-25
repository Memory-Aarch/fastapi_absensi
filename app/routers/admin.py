from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Attendance

admin_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@admin_router.get("/attendance")
def get_all_attendance(db: Session = Depends(get_db)):
    return db.query(Attendance).all()
