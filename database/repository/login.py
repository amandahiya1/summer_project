from sqlalchemy.orm import Session
from database.models.models import Students


def get_user(username: str, db: Session):
    user = db.query(Students).filter(Students.email == username).first()
    return user
