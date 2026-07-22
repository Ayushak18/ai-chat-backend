from app.repositories.user_repository import UserRepository
from fastapi import Depends, HTTPException
from app.services.auth_service import AuthService
from app.dependencies.repository import get_user_repository
from fastapi.security import OAuth2PasswordBearer
from app.database.models import User
from app.utils.jwt import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_auth_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(user_repository)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_repository: UserRepository = Depends(get_user_repository),
) -> User:

    payload = verify_access_token(token)
    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
        )

    user = user_repository.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
        )

    return user
