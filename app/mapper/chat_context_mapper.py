from app.database.models import Conversation, Message
from app.mapper.llm_mapper import build_llm_messages


def build_chat_context(
    conversation: Conversation,
    messages: list[Message],
) -> list[dict]:
    llm_messages = build_llm_messages(messages)

    if conversation.summary:
        llm_messages.insert(
            0,
            {
                "role": "system",
                "content": (
                    "Here is the summary of the earlier conversation. "
                    "Use it as context when answering the user.\n\n"
                    f"{conversation.summary}"
                ),
            },
        )

    return llm_messages
