import re


class InterviewEvaluator:
    """
    Temporary evaluator that works without an external LLM.

    Later this can be replaced with an LLM-based evaluator.
    """

    def evaluate(self, question, answer, objective):

        answer = (answer or "").strip()

        if not answer:
            return {
                "score": 0,
                "strengths": [],
                "gaps": ["No answer provided."],
                "feedback": "The candidate did not provide an answer."
            }

        words = re.findall(r"\b\w+\b", answer)
        word_count = len(words)

        score = 0
        strengths = []
        gaps = []

        # -----------------------------------------
        # Length / depth
        # -----------------------------------------

        if word_count >= 60:
            score += 4
            strengths.append(
                "Provided a detailed explanation."
            )

        elif word_count >= 30:
            score += 3
            strengths.append(
                "Provided a reasonable explanation."
            )

        elif word_count >= 10:
            score += 2
            strengths.append(
                "Provided a basic explanation."
            )

        else:
            score += 1
            gaps.append(
                "Answer needs more depth."
            )

        # -----------------------------------------
        # Technical vocabulary
        # -----------------------------------------

        technical_terms = [
            "python",
            "api",
            "model",
            "data",
            "database",
            "machine learning",
            "deep learning",
            "embedding",
            "vector",
            "llm",
            "rag",
            "algorithm",
            "neural",
            "training",
            "inference",
            "fastapi",
            "sql",
            "cloud",
            "docker"
        ]

        answer_lower = answer.lower()

        matched_terms = [
            term
            for term in technical_terms
            if term in answer_lower
        ]

        if matched_terms:

            score += 3

            strengths.append(
                "Used relevant technical terminology."
            )

        else:

            gaps.append(
                "Explanation could include more technical details."
            )

        # -----------------------------------------
        # Objective-specific signal
        # -----------------------------------------

        # Objective-specific signal
        objective_title = objective.get(
            "title",
            ""
        ).lower()

        # Topic keywords
        topic_keywords = {
            "python": [
                "python",
                "list",
                "tuple",
                "dictionary",
                "set",
                "mutable",
                "immutable"
            ],

            "programming": [
                "algorithm",
                "function",
                "variable",
                "loop",
                "complexity",
                "data structure"
            ],

            "data structures": [
                "array",
                "list",
                "stack",
                "queue",
                "tree",
                "graph",
                "hash",
                "complexity"
            ],

            "algorithms": [
                "algorithm",
                "complexity",
                "search",
                "sort",
                "array",
                "hash"
            ],

            "machine learning": [
                "model",
                "training",
                "prediction",
                "feature",
                "accuracy",
                "overfitting",
                "underfitting"
            ],

            "sql": [
                "sql",
                "query",
                "table",
                "join",
                "database",
                "index"
            ],

            "database": [
                "database",
                "table",
                "query",
                "index",
                "join",
                "sql"
            ]
        }

        matched = []

        for topic, keywords in topic_keywords.items():

            if topic in objective_title:

                matched = [
                    keyword
                    for keyword in keywords
                    if keyword in answer_lower
                ]

                break

        if matched:

            score += 3

            strengths.append(
                "Addressed the interview topic using relevant concepts."
            )

        else:

            gaps.append(
                "Answer could include more concepts related to the topic."
            )

        # -----------------------------------------
        # Final score
        # -----------------------------------------

        score = min(score, 10)

        if score >= 8:

            feedback = (
                "Strong answer. The candidate demonstrated "
                "good understanding."
            )

        elif score >= 5:

            feedback = (
                "Moderate answer. The candidate understands "
                "the basics but needs more depth."
            )

        else:

            feedback = (
                "Weak answer. The candidate should strengthen "
                "understanding of this topic."
            )

        return {
            "score": score,
            "strengths": strengths,
            "gaps": gaps,
            "feedback": feedback
        }