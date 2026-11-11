from components.terminal import Terminal

TERMINAL_OFFSETS = {
    "Resistor": [("left", -41.4, 2.2), ("right", 42.1, 2.2)],
    "Lamp": [("left", -25.5, 0.1), ("right", 25.6, 0.1)],
    "Ammeter": [("left", -25.5, 0.1), ("right", 25.6, 0.1)],
    "Voltmeter": [("left", -30.0, 0.4), ("right", 29.9, 0.4)],
    "Variable Resistor": [("left", -53.4, 3.4), ("right", 54.1, 3.4)],
    "Thermistor": [("left", -50.7, 0.8), ("right", 51.3, 0.8)],
    "Cell": [("left", -58.8, 1.5), ("right", 58.1, 1.5)],
    "Battery": [("left", -25.5, 0.1), ("right", 25.6, 0.1)],
    "Diode": [("left", -25.5, 0.1), ("right", 25.6, 0.1)],
    "LED": [("left", -29.4, 4.5), ("right", 29.9, 4.5)],
    "LDR": [("left", -26.9, 1.9), ("right", 28.6, 1.9)],
    "Fuse": [("left", -95.0, 0.4), ("right", 94.8, 0.4)],
    "Switch": [("left", -17.7, 0.6), ("right", 17.6, 0.6)]
}


class Component:

    def __init__(self, name: str, x: int = 0, y: int = 0) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.terminals = [Terminal(self, terminalName, xOffset, yOffset) for terminalName, xOffset, yOffset in TERMINAL_OFFSETS[self.name]]


    def getName(self) -> str:
        return f"Component: {self.name}"