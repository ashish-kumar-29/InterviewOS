class KnowledgeTracker:

    def __init__(self):
        self.topics = {}

    def update(self, topic, score):

        if score >= 8:
            status = "strong"
        elif score >= 5:
            status = "developing"
        else:
            status = "weak"

        self.topics[topic] = {
            "score": score,
            "status": status
        }

        return self.topics[topic]

    def get_topic(self, topic):

        return self.topics.get(
            topic,
            {
                "score": 0,
                "status": "unknown"
            }
        )

    def get_weak_topics(self):

        return [
            topic
            for topic, data in self.topics.items()
            if data["status"] == "weak"
        ]

    def get_strong_topics(self):

        return [
            topic
            for topic, data in self.topics.items()
            if data["status"] == "strong"
        ]

    def get_all(self):

        return self.topics