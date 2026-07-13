from sqlalchemy import select

from app.schemas.auth import RegisterRequest
from sqlalchemy.orm import Session
from app.database.models import User


class UserRepository:
    def __init__(self, db: Session):

        self.db = db

        # self.users = [
        #     {
        #         "id": 1,
        #         "name": "Ayush",
        #         "email": "ayush@gmail.com",
        #         "password": "password123",
        #     }
        # ]

    def create_user(self, request: RegisterRequest) -> User:
        print("Saving user to DB")
        new_user = User(
            name=request.name, email=request.email, password=request.password
        )

        # self.users.append(new_user)
        # adding to db session and committing the transaction
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)  # Refresh the instance to get the generated ID

        return new_user

    def get_user_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        result = self.db.execute(statement)

        return result.scalar_one_or_none()
        # for user in self.users:
        #     if user["email"] == email:
        #         return user
        # return None
