from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine

from app.models.user_model import User
from app.models.memory_model import Memory
from app.api.user_api import router as user_router
from app.api.auth_api import router as auth_router
from app.api.memory_api import router as memory_router
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Memora API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(memory_router)


@app.get("/")
def home():
    return {
        "message": "Memora Backend Running 🚀"
    }