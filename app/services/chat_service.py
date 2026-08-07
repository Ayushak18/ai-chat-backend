from app.services.conversation_service import ConversationService
from app.services.message_service import MessageService
from app.schemas.chat import ChatRequest, ChatResponse
from app.enum.message_role import MessageRole
from fastapi import HTTPException
from app.services.llm_service import LLMService
from app.database.models import Message
from collections.abc import Generator
from app.mapper.llm_mapper import build_llm_messages


class ChatService:
    def __init__(
        self,
        conversation_service: ConversationService,
        message_service: MessageService,
        llm_service: LLMService,
    ):
        self.conversation_service = conversation_service
        self.message_service = message_service
        self.llm_service = llm_service

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

        messages = self.message_service.get_messages_by_conversation_id(
            conversation_id=conversation.id,
            current_user_id=current_user_id,
        )

        llm_messages = build_llm_messages(messages=messages)

        assistant_reply = self.llm_service.generate_response(
            messages=llm_messages[-10:]
        )

        self.message_service.create_message(
            content=assistant_reply,
            conversation_id=conversation.id,
            role=MessageRole.ASSISTANT,
        )

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

        messages = self.message_service.get_messages_by_conversation_id(
            conversation_id=conversation.id,
            current_user_id=current_user_id,
        )

        llm_messages = build_llm_messages(messages=messages)

        stream = self.llm_service.generate_stream(messages=llm_messages[-5:])

        try:
            for chunk in stream:
                full_response += chunk
                yield chunk

            self.message_service.create_message(
                content=full_response,
                conversation_id=conversation.id,
                role=MessageRole.ASSISTANT,
            )
        except Exception as e:
            print(f"Streaming Error: {e}")
            raise
