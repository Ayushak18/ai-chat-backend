from groq import Groq
from app.config.settings import settings
from collections.abc import Generator


class LLMService:

    def __init__(self):
        self.client = Groq(api_key=settings.llm_api_key)

    def generate_response(self, messages: list[dict]) -> str:
        response = self.client.chat.completions.create(
            model=settings.llm_model,
            messages=messages,
        )

        return response.choices[0].message.content

    def generate_stream(self, messages: list[dict]) -> Generator[str, None, None]:
        stream = self.client.chat.completions.create(
            model=settings.llm_model, messages=messages, stream=True
        )
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content
