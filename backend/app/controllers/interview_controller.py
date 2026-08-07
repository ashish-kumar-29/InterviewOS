from app.loaders.candidate_loader import CandidateLoader
from app.loaders.curriculum_loader import CurriculumLoader

from app.agents.planner import InterviewPlanner
from app.memory.session_manager import SessionManager


class InterviewController:

    def __init__(self):

        self.candidate_loader = CandidateLoader()
        self.curriculum_loader = CurriculumLoader()

        self.planner = InterviewPlanner()

        self.sessions = SessionManager()

    def start(self, candidate_id):

        candidate = self.candidate_loader.get_candidate(candidate_id)

        curriculum = self.curriculum_loader.load()

        plan = self.planner.create_plan(
            candidate,
            curriculum
        )

        session = self.sessions.create_session(candidate_id)

        first_objective = plan["objectives"][0]

        question = (
            f"You skipped '{first_objective['title']}'. "
            "Explain this topic in detail."
        )

        self.sessions.add_question(
            session,
            question
        )

        return {
            "sessionId": session,
            "question": question,
            "done": False
        }