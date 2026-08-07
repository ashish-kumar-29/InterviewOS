from app.loaders.candidate_loader import CandidateLoader
from app.intelligence.candidate_intelligence import CandidateIntelligence

loader = CandidateLoader()

candidate = loader.get_candidate("CAND-001")

engine = CandidateIntelligence()

profile = engine.analyze(candidate)

print(profile)