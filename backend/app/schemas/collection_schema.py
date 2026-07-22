from datetime import datetime

from pydantic import BaseModel


class CollectionCreate(BaseModel):

    name: str


class CollectionUpdate(BaseModel):

    name: str


class CollectionResponse(BaseModel):

    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True

