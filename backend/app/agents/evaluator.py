class AnswerEvaluator:

    def evaluate(self, answer: str):

        score = 0

        if len(answer.split()) > 20:
            score += 30

        keywords = [
            "because",
            "example",
            "architecture",
            "tradeoff",
            "performance"
        ]

        for keyword in keywords:
            if keyword.lower() in answer.lower():
                score += 10

        score = min(score, 100)

        if score >= 80:
            level = "Strong"

        elif score >= 50:
            level = "Medium"

        else:
            level = "Weak"

        return {
            "score": score,
            "level": level
        }