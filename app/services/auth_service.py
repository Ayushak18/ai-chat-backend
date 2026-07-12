from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest


class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()

    def register(self, request: RegisterRequest):
        existing_user = self.user_repository.get_user_by_email(request.email)
        if existing_user:
            return {
                "message": "User with this email already exists.",
            }
        new_user = self.user_repository.create_user(request)
        return {
            "message": "User registered successfully.",
            "user": {
                "id": new_user["id"],
                "name": new_user["name"],
                "email": new_user["email"],
            },
        }
