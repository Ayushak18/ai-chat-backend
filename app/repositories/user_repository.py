from app.schemas.auth import RegisterRequest


class UserRepository:
    def __init__(self):

        self.users = [
            {
                "id": 1,
                "name": "Ayush",
                "email": "ayush@gmail.com",
                "password": "password123",
            }
        ]

    def create_user(self, request: RegisterRequest) -> dict:
        print("Saving user to DB")
        new_user = {
            "id": len(self.users) + 1,
            "name": request.name,
            "email": request.email,
            "password": request.password,
        }

        self.users.append(new_user)

        return new_user

    def get_user_by_email(self, email: str) -> dict | None:
        for user in self.users:
            if user["email"] == email:
                return user
        return None
