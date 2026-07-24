from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ConversationResponse(BaseModel):

    # Without from_attributes=True, Pydantic doesn’t know that it should read values like:
    # Without below line , these will be SQLAlchemy ORM objects.
    # This line does - If you receive a SQLAlchemy object, read its attributes.
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    updated_at: datetime
