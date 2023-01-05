from sqlalchemy.orm import Session
from database.schemas.schemas import CreateStudent
from database.models.models import Students

from hasher.hasher import Hasher


def create_new_student(student: CreateStudent, db: Session):
    student = Students(name=student.name,
                       email=student.email,
                       password=Hasher.hash_password(student.password))
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def list_students(db: Session):
    students = db.query(Students).all()
    return students


def get_student_by_id(s_id: int, db: Session):
    student = db.query(Students).filter(Students.s_id == s_id).first()
    return student


def delete_student_by_id(s_id: int, db: Session):
    existing_student = db.query(Students).filter(Students.s_id == s_id)
    if not existing_student.first():
        return False
    existing_student.delete(synchronize_session=False)
    db.commit()
    return True
