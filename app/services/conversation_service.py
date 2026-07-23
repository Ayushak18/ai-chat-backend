from app.repositories.conversation_repository import ConversationRepository
from app.database.models import Conversation


class ConversationService:

    def __init__(self, conversation_repository: ConversationRepository):
        self.conversation_repository = conversation_repository

    def create_conversation(self, title: str, user_id: int) -> Conversation:
        conversation = self.conversation_repository.create_conversation(title, user_id)
        return conversation

    def get_conversation_by_id(self, conversation_id: int) -> Conversation | None:
        return self.conversation_repository.get_conversation_by_id(conversation_id)

    def get_conversations_by_user_id(self, user_id: int) -> list[Conversation]:
        conversation = self.conversation_repository.get_conversations_by_user_id(
            user_id
        )
        return conversation
