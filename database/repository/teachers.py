from sqlalchemy.orm import Session
from database.schemas.schemas import CreateTeacher
from database.models.models import Teachers

from hasher.hasher import Hasher


def create_new_teacher(teacher: CreateTeacher, db: Session):
    teacher = Teachers(name=teacher.name,
                       email=teacher.email,
                       password=Hasher.hash_password(teacher.password))
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher


def list_teachers(db: Session):
    teachers = db.query(Teachers).all()
    return teachers


def get_teacher_by_id(t_id: int, db: Session):
    teacher = db.query(Teachers).filter(Teachers.t_id == t_id).first()
    return teacher


def delete_teacher_by_id(t_id: int, db: Session):
    existing_teacher = db.query(Teachers).filter(Teachers.t_id == t_id)
    if not existing_teacher.first():
        return False
    existing_teacher.delete(synchronize_session=False)
    db.commit()
    return True
