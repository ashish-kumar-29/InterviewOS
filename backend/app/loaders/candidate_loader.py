import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


class CandidateLoader:

    def __init__(self):
        self.candidates = self.load()

    def load(self):
        with open(DATA_DIR / "candidates.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        # Return only the candidate list
        return data["candidates"]

    

    def get_candidate(self, candidate_id):
        for candidate in self.candidates:
            if candidate["member"]["id"] == candidate_id:
                return candidate

        return None