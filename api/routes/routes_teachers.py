from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from database.schemas.schemas import TeacherBase, CreateTeacher

from database.session.session import get_db

from database.repository.teachers import create_new_teacher, delete_teacher_by_id, get_teacher_by_id, list_teachers

from database.models.models import Teachers

from api.routes.route_login import get_current_user


router = APIRouter(tags=["teacher"])


@router.post('/create_teacher', response_model=TeacherBase, status_code=status.HTTP_201_CREATED)
def create_teacher(teacher: CreateTeacher, db: Session = Depends(get_db)):
    teacher = create_new_teacher(teacher=teacher, db=db)
    return teacher


@router.get('/all_teachers', response_model=List[TeacherBase])
def get_all_teachers(db: Session = Depends(get_db)):
    result = list_teachers(db=db)
    teacher_list = []
    for teacher in result:
        teacher_list.append({"name": teacher.name, "email": teacher.email, "s_id": teacher.s_id})
    return teacher_list


@router.get('/teacher_by_id', response_model=TeacherBase)
def get_teacher(db: Session = Depends(get_db), current_user: Teachers = Depends(get_current_user)):
    teacher = get_teacher_by_id(t_id=current_user.t_id, db=db)
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Teacher with id:{current_user.t_id} "
                                                                          f"not exist")
    return teacher


@router.delete('/delete_teacher_by_id', status_code=status.HTTP_200_OK)
def delete_teacher(db: Session = Depends(get_db), current_user: Teachers = Depends(get_current_user)):
    deleted_teacher = delete_teacher_by_id(t_id=current_user.t_id, db=db)
    if not deleted_teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Teacher with id:{current_user.t_id} not found.")
    return {"msg": "Teacher deleted successfully."}
