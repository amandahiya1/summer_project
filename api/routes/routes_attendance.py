from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from database.schemas.schemas import AttendanceBase

from database.session.session import get_db

from database.repository.attendance import create_new_attendance, list_attendance, get_attendance_by_student, \
    get_attendance_by_subject

from database.models.models import Attendance

router = APIRouter(tags=["attendance"])


@router.post('/enter_attendance', response_model=AttendanceBase, status_code=status.HTTP_201_CREATED)
def enter_attendance(attendance: AttendanceBase, db: Session = Depends(get_db)):
    attendance = create_new_attendance(entry=attendance, db=db)
    return attendance


@router.get('/all_attendance', response_model=List[AttendanceBase])
def get_all_attendance(db: Session = Depends(get_db)):
    result = list_attendance(db=db)
    attendance_list = []
    for attendance in result:
        attendance_list.append({"a_id": attendance.a_id, "s_id": attendance.s_id, "sub_id": attendance.sub_id,
                                "date": attendance.date, "attendance": attendance.attendance})
    return attendance_list


@router.get('/attendance_by_students', response_model=List[AttendanceBase])
def get_attendance_by_students(s_id: int, db: Session = Depends(get_db)):
    result = get_attendance_by_student(s_id=s_id, db=db)
    attendance_list = []
    for attendance in result:
        attendance_list.append({"a_id": attendance.a_id, "s_id": attendance.s_id, "sub_id": attendance.sub_id,
                                "date": attendance.date, "attendance": attendance.attendance})
    return attendance_list


@router.get('/attendance_by_subject', response_model=List[AttendanceBase])
def get_attendance_by_subject(s_id: int, sub_id: int, db: Session = Depends(get_db)):
    result = get_attendance_by_subject(s_id=s_id, sub_id=sub_id, db=db)
    attendance_list = []
    for attendance in result:
        attendance_list.append({"a_id": attendance.a_id, "s_id": attendance.s_id, "sub_id": attendance.sub_id,
                                "date": attendance.date, "attendance": attendance.attendance})
    return attendance_list

