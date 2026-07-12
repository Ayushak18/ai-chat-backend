from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///chat.db"

engine = create_engine(DATABASE_URL)
