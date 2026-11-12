from components import Component
from circuit import Wire


class Circuit:
    def __init__(self, name: str) -> None:
        self.name = name
        self.components: list[Component] = []
        self.wires: list[Wire] = []

    def add_component(self, component: Component) -> None:
        self.components.append(component)

    def describe(self) -> str:
        return f"Circuit: {self.name}"


    #deleting components:

    def clear_components(self) -> None:
        self.components.clear()
        self.wires.clear()

    def remove_component(self, component: Component) -> None:
        if component in self.components:

            for terminal in component.terminals:
                for wire in terminal.wires.copy():
                    self.removeWire(wire)

            self.components.remove(component)

    #creating wires

    def addWire(self, wire: Wire) -> bool:
        self.wires.append(wire)
        wire.terminal1.wires.append(wire)
        wire.terminal2.wires.append(wire)

        return True

    def removeWire(self, wire: Wire) -> bool:
        if wire not in self.wires:
            return False

        self.wires.remove(wire)

        if wire not in wire.terminal1 or wire not in wire.terminal2:
            return False

        wire.terminal1.wires.remove(wire)
        wire.terminal2.wires.remove(wire)
        return True
    