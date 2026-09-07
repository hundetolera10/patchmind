from pydantic import BaseModel, Field


class AnalysisRequest(BaseModel):
    repository_path: str = Field(min_length=1)