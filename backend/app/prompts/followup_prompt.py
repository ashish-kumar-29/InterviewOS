class FollowupPrompt:

    def build(self, question, answer):

        return f"""
You are conducting a technical interview.

Original Question:
{question}

Candidate Answer:
{answer}

Generate ONE intelligent follow-up question.

Rules:

- Ask only ONE question.
- Focus on missing concepts.
- Do not explain.
- Do not provide hints.

Return ONLY the question.
"""