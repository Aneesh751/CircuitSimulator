import tkinter as tk
from gui import canvas


class MainGUI:

    def __init__(self) -> None:
        self.root = tk.Tk()

        self.root.title("CircuitSim")
        self.root.geometry("500x500")
        self.root.configure(bg="lightgray")
        self.root.state("zoomed")

        self.main = tk.Frame(self.root, bg="lightgray")
        self.canvas = canvas.Canvas(self.root, self)
        self.main.place(relheight=1, relwidth=1)
        self.canvas.place(relheight=1, relwidth=1)

        self.buildMainMenu()
        self.showMainMenu()

    def buildMainMenu(self) -> None:

        title = tk.Label(self.main, text="Circuit Simulator", font=("IBM Plex Sans", 40), bg="lightgray")
        title.pack(pady=50)
        start = tk.Button(self.main, text="Open Canvas", font=("IBM Plex Sans", 20), bg="gray", command=self.showCanvas)
        start.pack(pady=20)
        quit = tk.Button(self.main, text="Quit", font=("IBM Plex Sans", 20), bg="gray", command=self.root.quit)
        quit.pack(pady=20)

    def showMainMenu(self) -> None:
        self.root.title("CircuitSim")
        self.main.tkraise()
    def showCanvas(self) -> None:
        self.root.title("Circuit Canvas")
        self.canvas.tkraise()

    def setupWindow(self) -> None:
        self.root.mainloop()