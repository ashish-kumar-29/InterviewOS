from app.loaders.candidate_loader import CandidateLoader
from app.loaders.curriculum_loader import CurriculumLoader
from app.agents.planner import InterviewPlanner

candidate = CandidateLoader().get_candidate("CAND-001")

curriculum = CurriculumLoader().load()

planner = InterviewPlanner()

plan = planner.create_plan(candidate, curriculum)

print(plan)