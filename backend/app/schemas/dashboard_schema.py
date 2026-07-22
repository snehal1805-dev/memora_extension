from pydantic import BaseModel


class DashboardStats(BaseModel):

    total_memories: int
    favorite_memories: int
    today_memories: int
    total_domains: int