from pydantic import BaseModel
from typing import List, Optional


class Mission(BaseModel):
    day: int
    title: str

    passed: bool = False
    skipped: bool = False

    attempts: Optional[int] = None


class Signals(BaseModel):
    commitDays: int
    missionsCompleted: int
    missionsFirstTry: int


class Member(BaseModel):
    id: str
    name: str
    jobRole: str
    yearsExperience: int
    education: str


class Candidate(BaseModel):
    member: Member
    missions: List[Mission]
    signals: Signals