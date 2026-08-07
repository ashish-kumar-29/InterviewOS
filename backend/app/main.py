from fastapi import FastAPI
from app.api.interview import router as interview_router
from app.loaders.candidate_loader import CandidateLoader

loader = CandidateLoader()
# loader.get_candidate("candidate-001")

print(loader.get_candidate("CAND-001"))
print(loader.get_candidate("CAND-001")["member"]["name"])

app = FastAPI(
    title="InterviewOS",
    version="1.0.0",
)

app.include_router(interview_router)


@app.get("/")
def root():
    return {"message": "InterviewOS Backend Running"}