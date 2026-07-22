from pydantic import BaseModel


class InsightResponse(BaseModel):
    insight: str