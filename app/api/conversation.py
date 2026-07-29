from fastapi import APIRouter, Depends
from app.database.models import Conversation, User
from app.dependencies.auth import get_current_user
from app.dependencies.repository import get_conversation_service
from app.schemas.conversation import ConversationResponse
from app.services.conversation_service import ConversationService
from app.dependencies.repository import get_message_service
from app.services.message_service import MessageService
from app.schemas.message import MessageResponse

router = APIRouter(prefix="/conversations", tags=["conversation"])


@router.get("/", response_model=list[ConversationResponse])
def get_conversations(
    current_user: User = Depends(get_current_user),
    conversation_service: ConversationService = Depends(get_conversation_service),
) -> list[ConversationResponse]:

    conversations = conversation_service.get_conversations_by_user_id(current_user.id)
    return conversations


# why response_model ?
# Whatever I return, convert it into a list of MessageResponse
@router.get("/{conversation_id}/messages", response_model=list[MessageResponse])
def get_messages(
    conversation_id: int,
    current_user: User = Depends(get_current_user),
    message_service: MessageService = Depends(get_message_service),
) -> list[MessageResponse]:
    messages = message_service.get_messages_by_conversation_id(
        conversation_id=conversation_id, current_user_id=current_user.id
    )
    return messages
