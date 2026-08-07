from app.models.candidate import Candidate


class CandidateIntelligence:

    def analyze(self, candidate: Candidate):

        # Passed missions (used only for derived metrics)
        passed_missions = [
            m for m in candidate.missions
            if m.passed
        ]

        # Skipped missions
        skipped_missions = [
            m for m in candidate.missions
            if m.skipped
        ]

        # Topics that required more than one attempt
        retry_missions = [
            m for m in passed_missions
            if (m.attempts or 0) > 1
        ]

        # Interview difficulty
        if candidate.member.yearsExperience >= 8:
            difficulty = "Hard"
        elif candidate.member.yearsExperience >= 4:
            difficulty = "Medium"
        else:
            difficulty = "Easy"

        return {
            "candidate": candidate.member.name,
            "role": candidate.member.jobRole,
            "experience": candidate.member.yearsExperience,
            "difficulty": difficulty,

            # Official values from the dataset
            "completed": candidate.signals.missionsCompleted,
            "commit_days": candidate.signals.commitDays,
            "first_try": candidate.signals.missionsFirstTry,

            # Derived values
            "skipped": len(skipped_missions),
            "retry_topics": len(retry_missions),
        }