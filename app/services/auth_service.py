from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest
from app.utils.password import hash_password


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
