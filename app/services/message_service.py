from app.enum.message_role import MessageRole
from app.repositories.message_repository import MessageRepository
from app.database.models import Message
from app.services.conversation_service import ConversationService
from fastapi import HTTPException


class MessageService:
    def __init__(
        self,
        message_repository: MessageRepository,
        conversation_service: ConversationService,
    ):
        self.message_repository = message_repository
        self.conversation_service = conversation_service

    def create_message(
        self, content: str, conversation_id: int, role: MessageRole
    ) -> Message:
        message = self.message_repository.create_message(content, conversation_id, role)
        return message

    def get_messages_by_conversation_id(
        self, conversation_id: int, current_user_id: int
    ) -> list[Message]:
        conversation = self.conversation_service.get_conversation_by_id(conversation_id)
        if conversation is None:
            raise HTTPException(status_code=404, detail="Conversation not found")

        if conversation.user_id != current_user_id:
            raise HTTPException(status_code=404, detail="Conversation not found")

        messages = self.message_repository.get_messages_by_conversation_id(
            conversation_id
        )
        return messages

    def get_messages_after_message_id(
        self,
        conversation_id: int,
        message_id: int | None,
    ) -> list[Message]:
        return self.message_repository.get_messages_after_message_id(
            conversation_id=conversation_id, message_id=message_id
        )
