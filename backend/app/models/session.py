from pydantic import BaseModel, Field
from typing import Optional


class AskedQuestion(BaseModel):
    day: int
    topic: str
    objective: str

    question: str

    answer: Optional[str] = None

    score: Optional[int] = None

    followup_needed: bool = False


class InterviewSession(BaseModel):

    sessionId: str

    candidateId: str

    currentQuestion: int = 0

    totalQuestions: int = 0

    coveredDays: list[int] = Field(default_factory=list)

    questions: list[AskedQuestion] = Field(default_factory=list)

    objectivesCompleted: list[str] = Field(default_factory=list)

    completed: bool = False