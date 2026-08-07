import networkx as nx


class CurriculumGraph:

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_day(self, day_number, title, module):
        self.graph.add_node(
            day_number,
            title=title,
            module=module
        )

    def add_dependency(self, from_day, to_day):
        self.graph.add_edge(from_day, to_day)

    def next_days(self, day):
        return list(self.graph.successors(day))

    def previous_days(self, day):
        return list(self.graph.predecessors(day))