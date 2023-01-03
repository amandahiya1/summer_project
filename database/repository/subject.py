from sqlalchemy.orm import Session
from database.schemas.schemas import SubjectBase
from database.models.models import Subjects


def create_new_subject(subject: SubjectBase, db: Session):
    subject = Subjects(id=subject.sub_id,
                       name=subject.sub_name,
                       t_id=subject.t_id)
    db.add(subject)
    db.commit()
    db.refresh(subject)
    return subject


def list_subjects(db: Session):
    subjects = db.query(Subjects).all()
    return subjects


def delete_subject_by_id(sub_id: int, db: Session):
    existing_subject = db.query(Subjects).filter(Subjects.sub_id == sub_id)
    if not existing_subject.first():
        return False
    existing_subject.delete(synchronize_session=False)
    db.commit()
    return True
