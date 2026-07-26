from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.enum.message_role import MessageRole


class MessageResponse(BaseModel):
    # Allows FastAPI to serialize SQLAlchemy ORM objects automatically.
    model_config = ConfigDict(from_attributes=True)
    id: int
    content: str
    role: MessageRole
    created_at: datetime
