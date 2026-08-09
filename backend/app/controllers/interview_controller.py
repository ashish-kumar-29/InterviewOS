from app.loaders.curriculum_loader import CurriculumLoader
from app.memory.session_manager import SessionManager

from app.agents.interviewer import InterviewAgent
from app.agents.evaluator import InterviewEvaluator

from app.interview_engine.knowledge_tracker import KnowledgeTracker

from app.services.breeth_service import BreethService


class InterviewController:

    def __init__(self):

        self.curriculum_loader = CurriculumLoader()

        self.sessions = SessionManager()

        self.agent = InterviewAgent()

        self.evaluator = InterviewEvaluator()

        self.breeth = BreethService()

        self.knowledge = KnowledgeTracker()

    def process(self, request):

        # =================================================
        # START INTERVIEW
        # =================================================

        if request.candidate is not None:

            curriculum = self.curriculum_loader.load()

            candidate = request.candidate

            # Create interview plan
            interview = self.agent.start(
                candidate,
                curriculum
            )

            plan = interview["plan"]

            # Candidate ID
            candidate_id = candidate.member.id

            # Create session
            session_id = self.sessions.create_session(
                request.sessionId,
                candidate_id,
                plan
            )

            question = interview["prompt"]

            self.sessions.add_question(
                session_id,
                question
            )

            return {
                "reply": question,
                "done": False
            }

        # =================================================
        # CONTINUE INTERVIEW
        # =================================================

        session = self.sessions.get_session(
            request.sessionId
        )

        if session is None:

            return {
                "reply": "Invalid session.",
                "done": True
            }

        answer = request.message or ""

        current_index = session["current_index"]

        objectives = session["plan"]["objectives"]

        # Safety check
        if current_index >= len(objectives):

            self.sessions.complete(
                request.sessionId
            )

            return self._final_feedback(
                request.sessionId
            )

        # Current objective
        objective = objectives[current_index]

        # Current question
        if session["questions"]:

            question = session["questions"][-1]

        else:

            question = objective["title"]

        # -------------------------------------------------
        # Store answer
        # -------------------------------------------------

        self.sessions.add_answer(
            request.sessionId,
            answer
        )

        # -------------------------------------------------
        # Evaluate answer
        # -------------------------------------------------

        evaluation = self.evaluator.evaluate(
            question,
            answer,
            objective
        )

        self.sessions.add_evaluation(
            request.sessionId,
            evaluation
        )

        # -------------------------------------------------
        # Update knowledge
        # -------------------------------------------------

        topic = objective["title"]

        knowledge = self.knowledge.update(
            topic,
            evaluation["score"]
        )

        self.sessions.update_knowledge(
            request.sessionId,
            topic,
            knowledge
        )

        # -------------------------------------------------
        # Save to Breeth
        # -------------------------------------------------

        try:

            self.breeth.save_conversation(
                session["candidate_id"],
                question,
                answer,
                evaluation
            )

        except Exception as e:

            print(
                "Breeth memory error:",
                e
            )

        # -------------------------------------------------
        # Move to next objective
        # -------------------------------------------------

        next_index = self.sessions.next_question(
            request.sessionId
        )

        # -------------------------------------------------
        # Interview finished
        # -------------------------------------------------

        if next_index >= len(objectives):

            self.sessions.complete(
                request.sessionId
            )

            return self._final_feedback(
                request.sessionId
            )

        # -------------------------------------------------
        # Select next objective
        # -------------------------------------------------

        next_objective = objectives[next_index]

        # -------------------------------------------------
        # Adaptive behavior
        # -------------------------------------------------

        if evaluation["score"] < 5:

            question = (
                f"Let's revisit {topic}. "
                f"Can you explain {topic} again, "
                f"but this time focus on the key concepts "
                f"and practical examples?"
            )

        elif evaluation["score"] >= 8:

            question = (
                f"Let's move to {next_objective['title']}. "
                f"Since you demonstrated strong understanding "
                f"of the previous topic, let's go deeper. "
                f"Can you explain this concept in detail?"
            )

        else:

            question = (
                f"Let's move to {next_objective['title']}. "
                f"Can you explain this concept?"
            )

        self.sessions.add_question(
            request.sessionId,
            question
        )

        return {
            "reply": question,
            "done": False
        }

    # =====================================================
    # FINAL FEEDBACK
    # =====================================================

    def _final_feedback(self, session_id):

        session = self.sessions.get_session(
            session_id
        )

        evaluations = session["evaluations"]

        if evaluations:

            scores = [
                e["score"]
                for e in evaluations
            ]

            average_score = round(
                sum(scores) / len(scores),
                2
            )

        else:

            average_score = 0

        strengths = []

        gaps = []

        for evaluation in evaluations:

            strengths.extend(
                evaluation.get(
                    "strengths",
                    []
                )
            )

            gaps.extend(
                evaluation.get(
                    "gaps",
                    []
                )
            )

        # Remove duplicates
        strengths = list(dict.fromkeys(strengths))
        gaps = list(dict.fromkeys(gaps))

        weak_topics = self.knowledge.get_weak_topics()

        next_steps = [
            f"Review {topic}"
            for topic in weak_topics
        ]

        return {
            "reply": "Interview completed.",
            "done": True,
            "feedback": {
                "summary": (
                    f"Interview completed with an "
                    f"average score of {average_score}/10."
                ),
                "strengths": strengths,
                "gaps": gaps,
                "next": next_steps
            }
        }