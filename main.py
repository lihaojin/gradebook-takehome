from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.models.base import Base
from db.session import engine, SessionLocal
from db.initialize_db_data import initialize_db_data
import db.models

from api.routers import auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        initialize_db_data(db)
    finally:
        db.close()

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)