from sqlalchemy.orm import Session
from database.schemas.schemas import StudentBase, CreateStudent
from database.models.models import Students


def create_new_student(student: CreateStudent, db: Session):
    student = Students(name = student.name,
    email=student.email,
    password=student.password)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def list_students(db:Session):
    students = db.query(Students).all()
    return students
