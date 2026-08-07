import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"


class CurriculumLoader:

    def load(self):

        with open(DATA_DIR / "curriculum.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        print(type(data))

        if isinstance(data, dict):
            print(data.keys())

        return data