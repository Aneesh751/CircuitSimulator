class Component:


    def __init__(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return f"Component: {self.name}"