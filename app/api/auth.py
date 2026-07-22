from fastapi import APIRouter, Depends
from app.database.models import User
from app.dependencies.auth import get_auth_service, get_current_user
from app.repositories.user_repository import UserRepository
from app.schemas.auth import LoginRequest, RegisterRequest
from app.services.auth_service import AuthService

router = APIRouter()

# auth_service = AuthService(UserRepository)


@router.post("/register")
def register(
    request: RegisterRequest, auth_service: AuthService = Depends(get_auth_service)
):
    return auth_service.register(request)


@router.post("/login")
def login(request: LoginRequest, auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.login(request)


@router.get("/me")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "message": " Welcome to the protected route!",
        "user": {
            "id": current_user.id,
            "email": current_user.email,
            "name": current_user.name,
        },
    }
