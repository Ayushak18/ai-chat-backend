from sqlalchemy.orm import Session
from app.database.models import Conversation
from sqlalchemy import select


class ConversationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_conversation(self, title: str, user_id: int) -> Conversation:
        new_conversation = Conversation(title=title, user_id=user_id)

        self.db.add(new_conversation)
        self.db.commit()
        self.db.refresh(new_conversation)

        return new_conversation

    def get_conversation_by_id(self, conversation_id: int) -> Conversation | None:
        statement = select(Conversation).where(Conversation.id == conversation_id)
        result = self.db.execute(statement)
        return result.scalar_one_or_none()

    def get_conversations_by_user_id(self, user_id: int) -> list[Conversation]:
        statement = select(Conversation).where(Conversation.user_id == user_id)
        result = self.db.execute(statement)
        return result.scalars().all()
