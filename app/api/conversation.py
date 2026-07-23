from fastapi import APIRouter, Depends
from app.database.models import Conversation, User
from app.dependencies.auth import get_current_user
from app.dependencies.repository import get_conversation_service
from app.schemas.conversation import ConversationResponse
from app.services.conversation_service import ConversationService

router = APIRouter(prefix="/conversation", tags=["conversation"])


@router.get("/")
def get_conversations(
    current_user: User = Depends(get_current_user),
    conversation_service: ConversationService = Depends(get_conversation_service),
) -> list[ConversationResponse]:

    conversations = conversation_service.get_conversations_by_user_id(current_user.id)
    return conversations
