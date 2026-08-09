from app.llm.llm_client import LLMClient


class InterviewLLM:

    def __init__(self):
        self.client = LLMClient()

    def generate_question(self, prompt):
        return self.client.chat(prompt)

    def evaluate(self, prompt):
        return self.client.chat(prompt)

    def followup(self, prompt):
        return self.client.chat(prompt)

    def feedback(self, prompt):
        return self.client.chat(prompt)