import uuid


class SessionManager:

    def __init__(self):
        self.sessions = {}

    def create_session(self, candidate_id):

        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {
            "candidate_id": candidate_id,
            "questions": [],
            "answers": [],
            "covered_days": set(),
            "objectives_completed": [],
            "difficulty": None,
            "feedback": {}
        }

        return session_id

    def get_session(self, session_id):
        return self.sessions.get(session_id)

    def add_question(self, session_id, question):

        self.sessions[session_id]["questions"].append(question)

    def add_answer(self, session_id, answer):

        self.sessions[session_id]["answers"].append(answer)

    def cover_day(self, session_id, day):

        self.sessions[session_id]["covered_days"].add(day)

    def complete_objective(self, session_id, objective):

        self.sessions[session_id]["objectives_completed"].append(objective)