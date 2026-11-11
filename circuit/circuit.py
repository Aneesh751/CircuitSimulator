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

    def remove_component(self, component: Component) -> None:
        if component in self.components:
            self.components.remove(component)

    #creating wires

    def addWire(self, wire: Wire) -> bool:

         