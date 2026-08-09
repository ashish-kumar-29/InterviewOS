import os
import httpx
from dotenv import load_dotenv

load_dotenv()


class BreethService:

    def __init__(self):

        self.api_key = os.getenv("BREETH_API_KEY")

        self.base_url = (
            "https://api.thebreeth.com/v1"
        )

    def save_conversation(
        self,
        candidate_id,
        question,
        answer,
        evaluation
    ):

        if not self.api_key:
            print("Breeth API key not configured.")
            return None

        content = (
            f"Candidate {candidate_id} was asked: "
            f"{question}\n\n"
            f"Candidate answered: "
            f"{answer}\n\n"
            f"Evaluation score: "
            f"{evaluation.get('score', 0)}/10.\n"
            f"Strengths: "
            f"{', '.join(evaluation.get('strengths', []))}.\n"
            f"Gaps: "
            f"{', '.join(evaluation.get('gaps', []))}."
        )

        payload = {
            "content": content,
            "group_id": "default",
            "source_description": "InterviewOS",
            "extract_intent": False
        }

        response = httpx.post(
            f"{self.base_url}/episodes",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json=payload,
            timeout=30
        )

        print(
            "Breeth save status:",
            response.status_code
        )

        if response.status_code >= 400:
            print(
                "Breeth response:",
                response.text
            )
            return None

        return response.json()

    def search_memory(self, query):

        if not self.api_key:
            return []

        response = httpx.post(
            f"{self.base_url}/search",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "query": query,
                "limit": 5
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return data.get("edges", [])