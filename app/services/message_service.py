from app.enum.message_role import MessageRole
from app.repositories.message_repository import MessageRepository
from app.database.models import Message


class MessageService:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    def create_message(
        self, content: str, conversation_id: int, role: MessageRole
    ) -> Message:
        message = self.message_repository.create_message(content, conversation_id, role)
        return message

    def get_messages_by_conversation_id(self, conversation_id: int) -> list[Message]:
        messages = self.message_repository.get_messages_by_conversation_id(
            conversation_id
        )
        return messages
