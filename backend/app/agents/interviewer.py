from app.agents.planner import InterviewPlanner
from app.prompts.question_prompt import QuestionPrompt


class InterviewAgent:

    def __init__(self):

        self.planner = InterviewPlanner()
        self.prompt_builder = QuestionPrompt()

    def start(self, candidate, curriculum):

        plan = self.planner.create_plan(
            candidate,
            curriculum
        )

        if not plan["objectives"]:

            return {
                "plan": plan,
                "objective": None,
                "prompt": (
                    "Can you briefly introduce yourself "
                    "and describe your experience with AI systems?"
                )
            }

        objective = plan["objectives"][0]

        # Build prompt only for reference/logging
        prompt = self.prompt_builder.build(
            candidate,
            objective,
            {
                "difficulty": plan["difficulty"]
            }
        )

        # Generate a REAL interview question
        question = self.generate_question(objective)

        return {
            "plan": plan,
            "objective": objective,
            "prompt": question
        }

    def generate_question(self, objective):

        title = objective.get(
            "title",
            "this technical topic"
        )

        title_lower = title.lower()

        questions = {

            "python & programming fundamentals":
                "Explain the difference between a list, tuple, set, and dictionary in Python. When would you choose each one?",

            "data structures & algorithms":
                "How would you determine whether a given array contains duplicate elements, and what would be the time and space complexity of your approach?",

            "object oriented programming":
                "Explain the four major principles of object-oriented programming and give a practical example of each.",

            "database management":
                "What is the difference between an SQL JOIN and a subquery? Explain when you would prefer one over the other.",

            "machine learning":
                "Explain the difference between overfitting and underfitting in machine learning and describe two techniques to address overfitting.",

            "deep learning":
                "Explain how a neural network learns during training, including the role of forward propagation, loss, backpropagation, and gradient descent.",

            "large language models":
                "Explain how a transformer-based Large Language Model processes an input sequence and why the attention mechanism is important.",

            "generative ai":
                "What is Retrieval-Augmented Generation (RAG), and how does it help improve the reliability of responses from a Large Language Model?",

            "apis & backend":
                "Explain how you would design a REST API for a production application and discuss authentication, error handling, and scalability.",

            "fastapi":
                "Why would you use FastAPI for a Python backend? Explain how request validation and asynchronous endpoints work.",

            "cloud computing":
                "How would you deploy a Python-based machine learning API to the cloud, and what factors would you consider for scalability?",

            "sql":
                "What is database normalization? Explain the purpose of first, second, and third normal forms."
        }

        # Exact match
        if title_lower in questions:
            return questions[title_lower]

        # Partial match
        for topic, question in questions.items():

            if topic in title_lower:
                return question

        # Generic fallback
        return (
            f"Can you explain {title} in detail, "
            f"including its key concepts, practical applications, "
            f"and the trade-offs involved?"
        )