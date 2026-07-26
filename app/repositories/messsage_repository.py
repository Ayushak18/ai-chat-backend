from sqlalchemy.orm import Session
from app.enum.message_role import MessageRole
from app.database.models import Message
from sqlalchemy import select


class MessageRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_message(
        self, content: str, conversation_id: int, role: MessageRole
    ) -> Message:
        new_message = Message(
            content=content, conversation_id=conversation_id, role=role
        )
        self.db.add(new_message)
        self.db.commit()
        self.db.refresh(new_message)
        return new_message

    def get_messages_by_conversation_id(self, conversation_id: int) -> list[Message]:
        statement = (
            select(Message)
            .where(Message.conversation_id == conversation_id)
            .order_by(Message.created_at)
        )
        result = self.db.execute(statement)
        return result.scalars().all()
