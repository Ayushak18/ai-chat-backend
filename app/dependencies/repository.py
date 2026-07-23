from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.repositories.user_repository import UserRepository
from app.repositories.conversation_repository import ConversationRepository
from app.services.conversation_service import ConversationService


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
