import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


class CurriculumLoader:

    def __init__(self):
        self.curriculum = self.load()

    def load(self):
        with open(DATA_DIR / "curriculum.json", "r", encoding="utf-8") as f:
            return json.load(f)

    def get_modules(self):
        return self.curriculum