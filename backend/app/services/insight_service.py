from sqlalchemy.orm import Session
from collections import Counter

from app.models.memory_model import Memory
from app.core.groq_client import client

MODEL = "llama-3.3-70b-versatile"


def generate_ai_insight(
    db: Session,
    user_id: int
):

    memories = (
        db.query(Memory)
        .filter(Memory.user_id == user_id)
        .all()
    )

    if not memories:
        return {
            "insight": "No memories available."
        }

    total = len(memories)

    domains = [
        m.domain
        for m in memories
        if m.domain
    ]

    top_domain = (
        Counter(domains).most_common(1)[0][0]
        if domains else "Unknown"
    )

    tags = []

    for memory in memories:

        if memory.tags:

            tags.extend(
                [
                    tag.strip()
                    for tag in memory.tags.split(",")
                ]
            )

    top_tags = ", ".join(
        [
            tag
            for tag, _ in Counter(tags).most_common(5)
        ]
    )

    total_reading = sum(
        memory.reading_time or 0
        for memory in memories
    )

    prompt = f"""
Generate a short motivational insight.

Statistics

Total Memories: {total}

Top Domain: {top_domain}

Top Topics: {top_tags}

Estimated Reading Time: {total_reading} minutes

Return only one paragraph.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "insight": response.choices[0].message.content
    }