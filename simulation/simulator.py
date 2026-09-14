from graphs import GraphManager


class Simulator:
    def __init__(self, graph: GraphManager) -> None:
        self.graph = graph

    def run(self) -> str:
        return f"Simulation using {self.graph.describe()}"
