from groq import Groq
from app.config.settings import settings


class LLMService:

    def __init__(self):
        self.client = Groq(api_key=settings.llm_api_key)

    def generate_response(self, messages: list[dict]) -> str:
        response = self.client.chat.completions.create(
            model=settings.llm_model,
            messages=messages,
        )

        return response.choices[0].message.content
