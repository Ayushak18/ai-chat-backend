from app.services.conversation_service import ConversationService
from app.services.message_service import MessageService
from app.schemas.chat import ChatRequest, ChatResponse
from app.enum.message_role import MessageRole
from fastapi import HTTPException
from app.services.llm_service import LLMService
from collections.abc import Generator
from app.services.summary_service import SummaryService
from app.mapper.chat_context_mapper import build_chat_context


class ChatService:
    def __init__(
        self,
        conversation_service: ConversationService,
        message_service: MessageService,
        llm_service: LLMService,
        summary_service: SummaryService,
    ):
        self.conversation_service = conversation_service
        self.message_service = message_service
        self.llm_service = llm_service
        self.summary_service = summary_service

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

        messages = self.message_service.get_recent_messages_after_message_id(
            conversation_id=conversation.id,
            message_id=conversation.summary_upto_message_id,
            limit=10,
        )

        llm_messages = build_chat_context(
            conversation=conversation,
            messages=messages,
        )

        assistant_reply = self.llm_service.generate_response(
            messages=llm_messages,
        )

        self.message_service.create_message(
            content=assistant_reply,
            conversation_id=conversation.id,
            role=MessageRole.ASSISTANT,
        )

        if self.summary_service.should_summarize(conversation.id):
            self.summary_service.update_summary(conversation.id)

        return ChatResponse(
            message=assistant_reply,
            conversation_id=conversation.id,
        )

    def stream_chat(
        self,
        request: ChatRequest,
        current_user_id: int,
    ) -> Generator[str, None, None]:

        full_response = ""

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

        messages = self.message_service.get_recent_messages_after_message_id(
            conversation_id=conversation.id,
            message_id=conversation.summary_upto_message_id,
            limit=10,
        )

        llm_messages = build_chat_context(
            conversation=conversation,
            messages=messages,
        )

        stream = self.llm_service.generate_stream(messages=llm_messages)

        try:
            for chunk in stream:
                full_response += chunk
                yield chunk

            self.message_service.create_message(
                content=full_response,
                conversation_id=conversation.id,
                role=MessageRole.ASSISTANT,
            )
            if self.summary_service.should_summarize(conversation.id):
                self.summary_service.update_summary(conversation.id)
        except Exception as e:
            print(f"Streaming Error: {e}")
            raise
