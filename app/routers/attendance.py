from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Attendance, User
from app.schemas import AttendanceCreate, AttendanceResponse
from app.core.dependencies import get_current_user
from datetime import datetime

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.post("/", response_model=AttendanceResponse)
def create_attendance(
    attendance_data: AttendanceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_attendance = Attendance(
        user_id=current_user.id,
        check_in=attendance_data.check_in or datetime.utcnow(),
        check_out=attendance_data.check_out,
        status=attendance_data.status,
    )
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance

@router.get("/history", response_model=list[AttendanceResponse])
def get_attendance_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    history = db.query(Attendance).filter(Attendance.user_id == current_user.id).all()
    return history
