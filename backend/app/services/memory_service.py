from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.memory_model import Memory
from app.services.ai_service import (
    generate_summary,
    generate_tags,
    store_embedding
)
from app.services.ai_service import delete_embedding
from datetime import datetime
from datetime import timezone
from app.utils.reading_time import calculate_reading_time
from app.utils.domain import extract_domain

def save_memory(
    db: Session,
    user_id: int,
    title: str,
    url: str,
    favicon: str,
    raw_content: str
):

    existing_memory = (
        db.query(Memory)
        .filter(
            Memory.user_id == user_id,
            Memory.url == url
        )
        .first()
    )

    if existing_memory:

        from datetime import datetime
        from datetime import timezone

        existing_memory.last_opened = datetime.now(
            timezone.utc
        )

        existing_memory.visit_count += 1

        db.commit()
        db.refresh(existing_memory)

        return existing_memory

    summary = generate_summary(raw_content)

    tags = generate_tags(raw_content)

    reading_time = calculate_reading_time(raw_content)

    domain = extract_domain(url)

    from datetime import datetime
    from datetime import timezone

    memory = Memory(
        user_id=user_id,
        title=title,
        url=url,
        domain=domain,
        favicon=favicon,
        raw_content=raw_content,
        cleaned_content=raw_content,
        ai_summary=summary,
        tags=tags,
        reading_time=reading_time,
        last_opened=datetime.now(timezone.utc),
        visit_count=1
    )

    db.add(memory)
    db.commit()
    db.refresh(memory)

    store_embedding(
    memory.id,
    user_id,
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

def get_dashboard_stats(
    db: Session,
    user_id: int
):

    total_memories = (
        db.query(Memory)
        .filter(
            Memory.user_id == user_id
        )
        .count()
    )

    favorite_memories = (
        db.query(Memory)
        .filter(
            Memory.user_id == user_id,
            Memory.is_favorite == True
        )
        .count()
    )

    today = datetime.now(
        timezone.utc
    ).date()

    today_memories = (
        db.query(Memory)
        .filter(
            Memory.user_id == user_id
        )
        .all()
    )

    today_count = 0

    for memory in today_memories:

        if memory.created_at.date() == today:
            today_count += 1

    domains = set()

    all_memories = (
        db.query(Memory)
        .filter(
            Memory.user_id == user_id
        )
        .all()
    )

    for memory in all_memories:

        try:

            domain = memory.url.split("/")[2]

            domains.add(domain)

        except Exception:
            pass

    return {

        "total_memories": total_memories,

        "favorite_memories": favorite_memories,

        "today_memories": today_count,

        "total_domains": len(domains)

    }

def get_recent_memories(
    db: Session,
    user_id: int,
    limit: int = 5
):

    return (
        db.query(Memory)
        .filter(
            Memory.user_id == user_id
        )
        .order_by(
            Memory.created_at.desc()
        )
        .limit(limit)
        .all()
    )

def get_top_domains(
    db: Session,
    user_id: int
):

    return (
        db.query(
            Memory.domain,
            func.count(Memory.id).label("count")
        )
        .filter(
            Memory.user_id == user_id
        )
        .group_by(
            Memory.domain
        )
        .order_by(
            func.count(Memory.id).desc()
        )
        .limit(5)
        .all()
    )

def get_top_tags(
    db: Session,
    user_id: int
):

    memories = (
        db.query(Memory)
        .filter(Memory.user_id == user_id)
        .all()
    )

    tag_count = {}

    for memory in memories:

        if not memory.tags:
            continue

        tags = [tag.strip() for tag in memory.tags.split(",")]

        for tag in tags:

            if tag:
                tag_count[tag] = tag_count.get(tag, 0) + 1

    sorted_tags = sorted(
        tag_count.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_tags[:10]

def get_most_visited(
    db: Session,
    user_id: int
):

    return (
        db.query(Memory)
        .filter(
            Memory.user_id == user_id
        )
        .order_by(
            Memory.visit_count.desc()
        )
        .limit(10)
        .all()
    )