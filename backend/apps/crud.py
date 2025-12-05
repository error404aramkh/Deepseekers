from sqlalchemy.orm import Session
from . import models

def create_user(db: Session, name: str, email: str, password_hash: str):
    db_user = models.User(name=name, email=email, password_hash=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
