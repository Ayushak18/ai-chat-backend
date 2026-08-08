from app.database.models import Message


def build_llm_messages(messages: list[Message]) -> list[dict]:
    llm_messages = []

    for message in messages:

        llm_messages.append(
            {
                "role": message.role.value,
                "content": message.content,
            }
        )

    return llm_messages
