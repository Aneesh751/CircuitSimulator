from circuit import Circuit
from components import Component
from graphs import GraphManager
from gui import MainWindow
from simulation import Simulator


if __name__ == "__main__":
    component = Component("Example")
    circuit = Circuit("Example circuit")
    circuit.add_component(component)
    graph = GraphManager(circuit)
    simulator = Simulator(graph)
    window = MainWindow(simulator)
    window.show()