from fastapi import APIRouter, Depends
from app.dependencies.auth import get_auth_service
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest
from app.services.auth_service import AuthService

router = APIRouter()

# auth_service = AuthService(UserRepository)


@router.post("/register")
def register(
    request: RegisterRequest, auth_service: AuthService = Depends(get_auth_service)
):
    return auth_service.register(request)
