class EvaluationPrompt:

    def build(self, question, answer):

        return f"""
You are a Senior AI Engineering Interviewer.

Evaluate the candidate's answer.

Question:
{question}

Candidate Answer:
{answer}

Return ONLY valid JSON.

{{
    "score": 0,
    "strengths": [],
    "weaknesses": [],
    "missing_concepts": [],
    "followup_required": true
}}
"""