from app.database.models import Message


def build_summary_messages(
    current_summary: str | None,
    messages: list[Message],
) -> list[dict]:
    new_messages = "\n".join(
        f"{message.role.value}: {message.content}" for message in messages
    )
    return [
        {
            "role": "system",
            "content": (
                "You maintain a concise and factual summary of a conversation. "
                "Update the existing summary using the new messages. "
                "Preserve important user goals, decisions, preferences, "
                "technical details, constraints, and relevant context. "
                "Remove repetition, greetings, small talk, and irrelevant details. "
                "Do not invent information. "
                "Return only the updated summary."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Current Summary:\n"
                f"{current_summary or 'No existing summary.'}\n\n"
                f"New Messages:\n"
                f"{new_messages}"
            ),
        },
    ]
