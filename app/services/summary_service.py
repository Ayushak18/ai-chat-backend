from fastapi import HTTPException

from app.services.conversation_service import ConversationService
from app.services.message_service import MessageService
from app.services.llm_service import LLMService


class SummaryService:
    def __init__(
        self,
        conversation_service: ConversationService,
        message_service: MessageService,
        llm_service: LLMService,
    ):
        self.conversation_service = conversation_service
        self.message_service = message_service
        self.llm_service = llm_service

    def should_summarize(self, conversation_id: int) -> bool:
        conversation = self.conversation_service.get_conversation_by_id(conversation_id)

        if conversation is None:
            raise HTTPException(
                status_code=404,
                detail="Conversation not found",
            )

        messages = self.message_service.get_messages_after_message_id(
            conversation_id=conversation_id,
            message_id=conversation.summary_upto_message_id,
        )

        return len(messages) >= 20
