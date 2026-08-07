from app.loaders.curriculum_loader import CurriculumLoader
from app.graph.graph_builder import GraphBuilder

loader = CurriculumLoader()

curriculum = loader.load()

builder = GraphBuilder()

graph = builder.build(curriculum)

print("Nodes:", graph.graph.number_of_nodes())
print("Edges:", graph.graph.number_of_edges())

print(graph.next_days(11))