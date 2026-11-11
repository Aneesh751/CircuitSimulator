from components.terminal import Terminal

class Wire:
    def __init__(self, terminal1: Terminal, terminal2: Terminal) -> None:
        self.terminal1 = terminal1
        self.terminal2 = terminal2