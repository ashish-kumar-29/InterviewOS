class FeedbackPrompt:

    def build(self, history):

        return f"""
You are a Senior Engineering Interviewer.

Interview History:

{history}

Generate interview feedback.

Return ONLY valid JSON.

{{
    "summary":"",
    "strengths":[],
    "gaps":[],
    "next":[]
}}
"""