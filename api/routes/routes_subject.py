from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from database.schemas.schemas import SubjectBase

from database.session.session import get_db

from database.repository.subject import create_new_subject, list_subjects, delete_subject_by_id

from database.models.models import Subjects

router = APIRouter(tags=["subjects"])


@router.post('/create_subject', response_model=SubjectBase, status_code=status.HTTP_201_CREATED)
def create_subject(subject: SubjectBase, db: Session = Depends(get_db)):
    subject = create_new_subject(subject=subject, db=db)
    return subject


@router.get('/all_subjects', response_model=List[SubjectBase])
def get_all_subjects(db: Session = Depends(get_db)):
    result = list_subjects(db=db)
    subject_list = []
    for subject in result:
        subject_list.append({"sub_name": subject.sub_name, "sub_id": subject.sub_id, "t_id": subject.t_id})
    return subject_list


@router.delete('/delete_subject_by_id', status_code=status.HTTP_200_OK)
def delete_subject(sub_id: int, db: Session = Depends(get_db)):
    deleted_subject = delete_subject_by_id(sub_id=sub_id, db=db)
    if not deleted_subject:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Subject with id:{sub_id} not found.")
    return {"msg": "Subject deleted successfully."}
