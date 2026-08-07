from pydantic import BaseModel
from typing import Optional


class Feedback(BaseModel):
    summary: str
    strengths: list[str]
    gaps: list[str]
    next: list[str]


class InterviewResponse(BaseModel):
    sessionId: str
    reply: str
    done: bool
    feedback: Optional[Feedback] = None