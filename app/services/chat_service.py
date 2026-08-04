from app.services.conversation_service import ConversationService
from app.services.message_service import MessageService
from app.schemas.chat import ChatRequest, ChatResponse
from app.enum.message_role import MessageRole
from fastapi import HTTPException


class ChatService:
    def __init__(
        self, conversation_service: ConversationService, message_service: MessageService
    ):
        self.conversation_service = conversation_service
        self.message_service = message_service

    def chat(
        self,
        request: ChatRequest,
        current_user_id: int,
    ) -> ChatResponse:
        if request.conversation_id is None:
            conversation = self.conversation_service.create_conversation(
                title="New Chat", user_id=current_user_id
            )

        else:
            conversation = self.conversation_service.get_conversation_by_id(
                request.conversation_id
            )
            if conversation is None or conversation.user_id != current_user_id:
                raise HTTPException(status_code=404, detail="Conversation not found")

        self.message_service.create_message(
            content=request.message,
            conversation_id=conversation.id,
            role=MessageRole.USER,
        )

        self.message_service.create_message(
            content="Hello! I'm your AI assistant.",
            conversation_id=conversation.id,
            role=MessageRole.ASSISTANT,
        )

        return ChatResponse(
            message="Hello! I'm your AI assistant.",
            conversation_id=conversation.id,
        )
