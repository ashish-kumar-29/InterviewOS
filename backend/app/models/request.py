from pydantic import BaseModel
from typing import Optional


class InterviewRequest(BaseModel):
    sessionId: Optional[str] = None
    candidateId: Optional[str] = None
    message: Optional[str] = None