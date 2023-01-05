from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from database.schemas.schemas import StudentBase, CreateStudent

from database.session.session import get_db

from database.repository.students import create_new_student, list_students, get_student_by_id, delete_student_by_id

from database.models.models import Students

from api.routes.route_login import get_current_user


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
def get_student(db: Session = Depends(get_db), current_user: Students = Depends(get_current_user)):
    student = get_student_by_id(s_id=current_user.s_id, db=db)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id:{current_user.s_id} "
                                                                          f"not exist")
    return student


@router.delete('/delete_student_by_id', status_code=status.HTTP_200_OK)
def delete_student(db: Session = Depends(get_db), current_user: Students = Depends(get_current_user)):
    deleted_user = delete_student_by_id(s_id=current_user.s_id, db=db)
    if not deleted_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{current_user.s_id} not found.")
    return {"msg": "User deleted successfully."}
