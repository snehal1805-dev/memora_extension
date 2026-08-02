import os

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine

# Import models so SQLAlchemy registers them before creating tables
from app.models.user_model import User
from app.models.memory_model import Memory
from app.models.collection_model import Collection

# Routers
from app.api.auth_api import router as auth_router
from app.api.user_api import router as user_router
from app.api.memory_api import router as memory_router
from app.api.chat_api import router as chat_router
from app.api.collection_api import router as collection_router

load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI Application
app = FastAPI(
    title="Memora API",
    version="1.0.0"
)

# CORS Origins
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "*"
).split(",")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(memory_router)
app.include_router(chat_router)
app.include_router(collection_router)


@app.get("/")
def home():
    return {
        "message": "Memora Backend Running 🚀"
    }