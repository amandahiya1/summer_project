from sqlalchemy.orm import Session
from database.models.models import Students, Teachers


def get_user(username: str, db: Session):
    user = db.query(Students).filter(Students.email == username).first()
    if not user:
        user = db.query(Teachers).filter(Teachers.email == username).first()
    return user
