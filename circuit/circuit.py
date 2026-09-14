from components import Component


class Circuit:
    def __init__(self, name: str) -> None:
        self.name = name
        self.components: list[Component] = []

    def add_component(self, component: Component) -> None:
        self.components.append(component)

    def describe(self) -> str:
        return f"Circuit: {self.name}"
