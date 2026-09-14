from circuit import Circuit


class GraphManager:
    def __init__(self, circuit: Circuit) -> None:
        self.circuit = circuit

    def describe(self) -> str:
        return f"Graph for {self.circuit.name}"
