class Component:


    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        return f"Component: {self.name}"