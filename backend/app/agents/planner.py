from app.intelligence.candidate_intelligence import CandidateIntelligence


class InterviewPlanner:

    def create_plan(self, candidate, curriculum):

        intelligence = CandidateIntelligence()

        profile = intelligence.analyze(candidate)

        difficulty = profile["difficulty"]

        objectives = []

        # Always include skipped missions first
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

        return {

            "candidate": profile,

            "difficulty": difficulty,

            "minimum_questions": 8,

            "minimum_curriculum_days": 4,

            "objectives": objectives
        }