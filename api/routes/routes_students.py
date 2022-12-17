from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from database.schemas.schemas import StudentBase, CreateStudent

from database.session.session import get_db

from database.repository.students import create_new_student, list_students, get_student_by_id

from database.models.models import Students



router = APIRouter(tags=["student"])


@router.post('/create_student', response_model=StudentBase, status_code=status.HTTP_201_CREATED)
def create_student(student: CreateStudent, db: Session = Depends(get_db)):
    student = create_new_student(student=student, db=db)
    return student

@router.get('/all_students', response_model=List[StudentBase])
def get_all_students(db: Session = Depends(get_db)):
    result = list_students(db=db)
    student_list = []
    for student in result:
        student_list.append({"name": student.name, "email": student.email, "s_id": student.s_id})
    return student_list


@router.get('/student_by_id', response_model=StudentBase)
def get_student(db: Session = Depends(get_db)):
    student = get_student_by_id(s_id = 9, db=db)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id not exist")
    return student

