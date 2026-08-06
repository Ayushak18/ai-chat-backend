from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine

from app.api.auth import router as auth_router
from app.api.conversation import router as conversation_router
from app.api.chat import router as chat_router
from app.api.stream import router as stream_router

# Import models so they register with Base
from app.database import models

app = FastAPI()

# Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(conversation_router)
app.include_router(chat_router)
app.include_router(stream_router)
