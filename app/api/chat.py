from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.database.models import User
from app.services.chat_service import ChatService
from app.dependencies.repository import get_chat_service
from app.schemas.chat import ChatResponse, ChatRequest

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    chat_service: ChatService = Depends(get_chat_service),
) -> ChatResponse:
    response = chat_service.chat(
        request,
        current_user_id=current_user.id,
    )
    return response
