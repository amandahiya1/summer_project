from sqlalchemy.orm import Session
from database.schemas.schemas import AttendanceBase
from database.models.models import Attendance


def create_new_attendance(entry: AttendanceBase, db: Session):
    entry = Attendance(a_id=entry.a_id,
                       s_id=entry.s_id,
                       sub_id=entry.sub_id,
                       date=entry.date,
                       attendance=entry.attendance)

    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def list_attendance(db: Session):
    attendance = db.query(Attendance).all()
    return attendance


def get_attendance_by_student(s_id: int, db: Session):
    attendance = db.query(Attendance).filter(Attendance.s_id == s_id).all()
    return attendance


def get_attendance_by_subject(s_id: int, sub_id: int, db: Session):
    attendance = db.query(Attendance).filter(Attendance.s_id == s_id, Attendance.sub_id == sub_id).all()
    return attendance
