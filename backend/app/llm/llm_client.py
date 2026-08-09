class LLMClient:
    """
    Temporary local LLM client.

    This allows InterviewOS development without an external
    LLM API. Later, replace chat() with the OpenRouter call.
    """

    def chat(self, prompt: str) -> str:

        # Temporary stub
        return prompt