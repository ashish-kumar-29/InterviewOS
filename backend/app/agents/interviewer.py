from app.agents.planner import InterviewPlanner


class InterviewEngine:

    def __init__(self):
        self.planner = InterviewPlanner()

    def start(self, candidate, curriculum):

        plan = self.planner.create_plan(
            candidate,
            curriculum
        )

        first = plan["objectives"][0]

        question = (
            f"You skipped '{first['title']}'. "
            f"Can you explain the core concepts behind this topic?"
        )

        return {
            "plan": plan,
            "question": question
        }