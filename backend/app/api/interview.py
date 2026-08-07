from fastapi import APIRouter
import uuid

from app.models.request import InterviewRequest
from app.models.response import InterviewResponse

router = APIRouter(prefix="/api", tags=["Interview"])


@router.post("/interview", response_model=InterviewResponse)
def interview(request: InterviewRequest):

    session_id = request.sessionId or str(uuid.uuid4())

    if request.message is None:
        return InterviewResponse(
            sessionId=session_id,
            reply="Welcome to InterviewOS! Let's begin. Can you briefly introduce yourself and your AI engineering background?",
            done=False,
        )

    return InterviewResponse(
        sessionId=session_id,
        reply="Thanks! (Mock Response) Next question will be generated here.",
        done=False,
    )