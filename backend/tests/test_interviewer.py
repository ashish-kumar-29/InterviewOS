from app.loaders.candidate_loader import CandidateLoader
from app.loaders.curriculum_loader import CurriculumLoader
from app.agents.interviewer import InterviewEngine

candidate = CandidateLoader().get_candidate("CAND-001")

curriculum = CurriculumLoader().load()

engine = InterviewEngine()

result = engine.start(candidate, curriculum)

print(result["question"])