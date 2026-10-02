class Component:

    def __init__(self, name: str, x: int = 0, y: int = 0) -> None:
        self.name = name
        self.x = x
        self.y = y

    def getName(self) -> str:
        return f"Component: {self.name}"