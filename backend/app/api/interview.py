from fastapi import APIRouter

from app.controllers.interview_controller import InterviewController
from app.models.request import InterviewRequest

router = APIRouter(prefix="/api", tags=["Interview"])

controller = InterviewController()


@router.post("/interview")
def interview(request: InterviewRequest):

    if request.sessionId is None:

        return controller.start(request.candidateId)

    return {
        "message": "Continue interview coming next..."
    }