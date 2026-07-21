from fastapi import HTTPException

from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, RegisterRequest
from app.utils.password import hash_password, verify_password
from app.utils.jwt import create_access_token


class AuthService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register(self, request: RegisterRequest):
        existing_user = self.user_repository.get_user_by_email(request.email)
        if existing_user:
            return {
                "message": "User with this email already exists.",
            }
        request.password = hash_password(request.password)
        new_user = self.user_repository.create_user(request)
        return {
            "message": "User registered successfully.",
            "user": {
                "id": new_user.id,
                "name": new_user.name,
                "email": new_user.email,
            },
        }

    def login(self, request: LoginRequest):
        user = self.user_repository.get_user_by_email(request.email)

        if user is None:
            raise HTTPException(status_code=401, detail="Invalid email or password.")

        if not verify_password(request.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid email or password.")

        access_token = create_access_token({"sub": str(user.id)})

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }
