from app.graph.curriculum_graph import CurriculumGraph


class GraphBuilder:

    def build(self, curriculum):

        graph = CurriculumGraph()

        # Build module lookup
        module_lookup = {}

        for module in curriculum["modules"]:
            for day in module["days"]:
                module_lookup[day] = module["title"]

        # Add all days
        for day in curriculum["days"]:

            graph.add_day(
                day["day"],
                day["title"],
                module_lookup.get(day["day"], "Unknown")
            )

        # Connect consecutive days
        sorted_days = sorted(
            curriculum["days"],
            key=lambda x: x["day"]
        )

        for i in range(len(sorted_days) - 1):

            graph.add_dependency(
                sorted_days[i]["day"],
                sorted_days[i + 1]["day"]
            )

        return graph