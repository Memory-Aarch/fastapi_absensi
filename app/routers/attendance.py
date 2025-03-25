from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Attendance
from datetime import datetime

attendance_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@attendance_router.post("/check-in")
def check_in(user_id: int, db: Session = Depends(get_db)):
    today = datetime.utcnow().date()
    if db.query(Attendance).filter(Attendance.user_id == user_id, Attendance.date == today).first():
        raise HTTPException(status_code=400, detail="Sudah check-in hari ini")

    new_attendance = Attendance(user_id=user_id, date=today, check_in_time=datetime.utcnow())
    db.add(new_attendance)
    db.commit()
    return {"msg": "Check-in berhasil"}

@attendance_router.post("/check-out")
def check_out(user_id: int, db: Session = Depends(get_db)):
    today = datetime.utcnow().date()
    attendance = db.query(Attendance).filter(Attendance.user_id == user_id, Attendance.date == today).first()

    if not attendance:
        raise HTTPException(status_code=400, detail="Belum check-in hari ini")

    attendance.check_out_time = datetime.utcnow()
    db.commit()
    return {"msg": "Check-out berhasil"}
