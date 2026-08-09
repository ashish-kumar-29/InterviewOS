from fastapi import FastAPI
from app.api.interview import router as interview_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="InterviewOS",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(interview_router)


@app.get("/")
def root():
    return {
        "message": "InterviewOS Backend Running"
    }