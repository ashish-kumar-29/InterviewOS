from copy import deepcopy


class SessionManager:

    def __init__(self):
        self.sessions = {}

    def create_session(self, session_id, candidate_id, plan):

        self.sessions[session_id] = {
            "candidate_id": candidate_id,
            "plan": deepcopy(plan),
            "current_index": 0,
            "questions": [],
            "answers": [],
            "evaluations": [],
            "scores": [],
            "knowledge": {},
            "covered_days": set(),
            "completed": False
        }

        return session_id

    def get_session(self, session_id):
        return self.sessions.get(session_id)

    def add_question(self, session_id, question):

        session = self.sessions.get(session_id)

        if session:
            session["questions"].append(question)

    def add_answer(self, session_id, answer):

        session = self.sessions.get(session_id)

        if session:
            session["answers"].append(answer)

    def add_evaluation(self, session_id, evaluation):

        session = self.sessions.get(session_id)

        if session:
            session["evaluations"].append(evaluation)
            session["scores"].append(
                evaluation.get("score", 0)
            )

    def update_knowledge(
        self,
        session_id,
        topic,
        knowledge
    ):

        session = self.sessions.get(session_id)

        if session:
            session["knowledge"][topic] = knowledge

    def next_question(self, session_id):

        session = self.sessions.get(session_id)

        if not session:
            return 0

        session["current_index"] += 1

        return session["current_index"]

    def complete(self, session_id):

        session = self.sessions.get(session_id)

        if session:
            session["completed"] = True