from sqlalchemy.orm import Session
from schemas.schemas import StudentBase
from database.models.models import Students


def create_new_student(student: StudentBase, db: Session, s_id: int):
    student = Students(**student.dict(), s_id=s_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

    