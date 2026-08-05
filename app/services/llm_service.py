from groq import Groq
from app.config.settings import settings


class LLMService:

    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)

    def generate_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=settings.llm_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content
