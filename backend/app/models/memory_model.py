from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Memory(Base):
    __tablename__ = "memories"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    title = Column(
        String(500),
        nullable=False
    )

    url = Column(
        Text,
        nullable=False
    )

    favicon = Column(
        Text,
        nullable=True
    )

    raw_content = Column(
        Text,
        nullable=False
    )

    cleaned_content = Column(
        Text,
        nullable=True
    )

    ai_summary = Column(
        Text,
        nullable=True
    )

    tags = Column(
        String(500),
        nullable=True
    )

    is_favorite = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    owner = relationship(
        "User",
        backref="memories"
    )