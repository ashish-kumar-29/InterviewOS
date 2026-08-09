class KnowledgeTracker:

    def initialize(self, plan):

        graph = {}

        for objective in plan["objectives"]:

            graph[objective["title"]] = {
                "score": None,
                "asked": False,
                "completed": False,
                "followup": False
            }

        return graph

    def update(self, graph, topic, score):

        if topic not in graph:
            return graph

        graph[topic]["score"] = score
        graph[topic]["asked"] = True

        if score >= 7:
            graph[topic]["completed"] = True
            graph[topic]["followup"] = False
        else:
            graph[topic]["completed"] = False
            graph[topic]["followup"] = True

        return graph