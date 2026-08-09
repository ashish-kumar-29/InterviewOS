from typing import Optional
from pydantic import BaseModel
from app.models.candidate import Candidate


class InterviewRequest(BaseModel):
    sessionId: str
    candidate: Optional[Candidate] = None
    message: Optional[str] = None