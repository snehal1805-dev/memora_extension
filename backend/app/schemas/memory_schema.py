from datetime import datetime
from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from pydantic import ConfigDict


class MemoryCreate(BaseModel):
    title: str
    url: str
    favicon: Optional[str] = None
    raw_content: str


class MemoryUpdate(BaseModel):
    tags: Optional[str] = None
    is_favorite: Optional[bool] = None


class MemoryResponse(BaseModel):
    id: int
    title: str
    url: str
    favicon: Optional[str]
    raw_content: str
    cleaned_content: Optional[str]
    ai_summary: Optional[str]
    tags: Optional[str]
    is_favorite: bool
    created_at: datetime
    reading_time: int
    domain: str | None
    last_opened: datetime | None
    visit_count: int

    model_config = ConfigDict(
        from_attributes=True
    )