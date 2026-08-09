from app.intelligence.candidate_intelligence import CandidateIntelligence


class InterviewPlanner:

    def create_plan(self, candidate, curriculum):

        intelligence = CandidateIntelligence()

        profile = intelligence.analyze(candidate)

        difficulty = profile["difficulty"]

        objectives = []

        # Existing skipped missions
        for mission in candidate.missions:

            if mission.skipped:

                objectives.append({
                    "type": "revisit",
                    "day": mission.day,
                    "title": mission.title,
                    "priority": "HIGH"
                })

        # Retry topics
        for mission in candidate.missions:

            if mission.passed and (mission.attempts or 0) > 1:

                objectives.append({
                    "type": "verify",
                    "day": mission.day,
                    "title": mission.title,
                    "priority": "MEDIUM"
                })

        # Strong topics
        for mission in candidate.missions:

            if mission.passed and (mission.attempts or 0) == 1:

                objectives.append({
                    "type": "challenge",
                    "day": mission.day,
                    "title": mission.title,
                    "priority": "LOW"
                })

        # -----------------------------------------
        # FALLBACK OBJECTIVES
        # -----------------------------------------

        fallback_topics = [
            "Python & Programming Fundamentals",
            "Data Structures & Algorithms",
            "SQL & Database Systems",
            "Machine Learning Fundamentals",
            "APIs & Backend Development",
            "System Design",
            "AI & LLM Concepts",
            "Problem Solving & Debugging"
        ]

        existing_titles = {
            obj["title"]
            for obj in objectives
        }

        for topic in fallback_topics:

            if topic not in existing_titles:

                objectives.append({
                    "type": "technical",
                    "day": len(objectives) + 1,
                    "title": topic,
                    "priority": "MEDIUM"
                })

        # Exactly enough for an interview
        objectives = objectives[:8]

        return {
            "candidate": profile,
            "difficulty": difficulty,
            "minimum_questions": 8,
            "minimum_curriculum_days": 4,
            "objectives": objectives
        }