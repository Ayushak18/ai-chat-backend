from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.repositories.user_repository import UserRepository


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)
