from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.repositories.user_repository import UserRepository
from app.repositories.conversation_repository import ConversationRepository
from app.services.conversation_service import ConversationService
from app.repositories.message_repository import MessageRepository
from app.services.message_service import MessageService
from app.services.chat_service import ChatService
from app.services.llm_service import LLMService
from app.services.summary_service import SummaryService


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
    conversation_service: ConversationService = Depends(get_conversation_service),
) -> MessageService:
    return MessageService(message_repository, conversation_service)


def get_llm_service() -> LLMService:
    return LLMService()


def get_summary_service(
    conversation_service: ConversationService = Depends(get_conversation_service),
    message_service: MessageService = Depends(get_message_service),
    llm_service: LLMService = Depends(get_llm_service),
) -> SummaryService:
    return SummaryService(
        conversation_service,
        message_service,
        llm_service,
    )


def get_chat_service(
    conversation_service: ConversationService = Depends(get_conversation_service),
    message_service: MessageService = Depends(get_message_service),
    llm_service: LLMService = Depends(get_llm_service),
    summary_service: SummaryService = Depends(get_summary_service),
) -> ChatService:
    return ChatService(
        conversation_service, message_service, llm_service, summary_service
    )
