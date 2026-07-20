from sqlalchemy.orm import Session

from app.models.memory_model import Memory
from app.services.ai_service import (
    generate_summary,
    store_embedding
)
from app.services.ai_service import delete_embedding

def save_memory(
    db: Session,
    user_id: int,
    title: str,
    url: str,
    favicon: str,
    raw_content: str
):

    summary = generate_summary(raw_content)

    memory = Memory(
        user_id=user_id,
        title=title,
        url=url,
        favicon=favicon,
        raw_content=raw_content,
        cleaned_content=raw_content,
        ai_summary=summary
    )

    db.add(memory)
    db.commit()
    db.refresh(memory)

    store_embedding(
        memory.id,
        memory.title,
        raw_content
    )

    return memory

def get_all_memories(
    db: Session,
    user_id: int
):

    return (
        db.query(Memory)
        .filter(Memory.user_id == user_id)
        .order_by(Memory.created_at.desc())
        .all()
    )


def get_memory_by_id(
    db: Session,
    user_id: int,
    memory_id: int
):

    return (
        db.query(Memory)
        .filter(
            Memory.id == memory_id,
            Memory.user_id == user_id
        )
        .first()
    )


def delete_memory(
    db: Session,
    memory: Memory
):

    delete_embedding(memory.id)

    db.delete(memory)

    db.commit()

def get_favorite_memories(
    db: Session,
    user_id: int
):

    return (
        db.query(Memory)
        .filter(
            Memory.user_id == user_id,
            Memory.is_favorite == True
        )
        .order_by(Memory.created_at.desc())
        .all()
    )

def update_memory(
    db: Session,
    memory: Memory,
    tags: str | None = None
):

    if tags is not None:
        memory.tags = tags

    db.commit()
    db.refresh(memory)

    return memory

def toggle_favorite(
    db: Session,
    memory: Memory
):

    memory.is_favorite = not memory.is_favorite

    db.commit()
    db.refresh(memory)

    return memory