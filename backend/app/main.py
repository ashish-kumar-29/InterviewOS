from fastapi import FastAPI
from app.api.interview import router as interview_router

app = FastAPI(
    title="InterviewOS",
    version="1.0.0",
)

app.include_router(interview_router)


@app.get("/")
def root():
    return {
        "message": "InterviewOS Backend Running"
    }