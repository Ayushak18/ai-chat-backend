from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine

from app.api.auth import router as auth_router

# Import models so they register with Base
from app.database import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
