from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.database import Base, engine
from app.database.connect_redis import connect_redis



@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)
    connect_redis()

    yield

    print("Application shutdown")



app = FastAPI(
    title="Pulsebet crypto betting app",
    version="1.0.0"
)