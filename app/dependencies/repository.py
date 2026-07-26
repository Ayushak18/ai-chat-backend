from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.repositories.user_repository import UserRepository
from app.repositories.conversation_repository import ConversationRepository
from app.services.conversation_service import ConversationService
from app.repositories.message_repository import MessageRepository
from app.services.message_service import MessageService


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_conversation_repository(
    db: Session = Depends(get_db),
) -> ConversationRepository:
    return ConversationRepository(db)


def get_conversation_service(
    conversation_repository: ConversationRepository = Depends(
        get_conversation_repository
    ),
) -> ConversationService:
    return ConversationService(conversation_repository)


def get_message_repository(db: Session = Depends(get_db)) -> MessageRepository:
    return MessageRepository(db)


def get_message_service(
    message_repository: MessageRepository = Depends(get_message_repository),
) -> MessageService:
    return MessageService(message_repository)
