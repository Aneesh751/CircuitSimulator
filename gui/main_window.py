from simulation import Simulator


class MainWindow:
    def __init__(self, simulator: Simulator) -> None:
        self.simulator = simulator

    def show(self) -> None:
        print(self.simulator.run())
