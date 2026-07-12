from fastapi import APIRouter
from app.schemas.auth import RegisterRequest
from app.services.auth_service import AuthService

router = APIRouter()

auth_service = AuthService()


@router.post("/register")
def register(
    request: RegisterRequest,
):
    return auth_service.register(request)
