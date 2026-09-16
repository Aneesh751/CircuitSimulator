import tkinter as tk
from gui import canvas



class MainGUI:

    def __init__(self) -> None:
        self.canvas = canvas.Canvas()


    def openWindow(self) -> None:
        root = tk.Tk()
        root.title("CircuitSim")
        root.geometry("500x500")
        root.configure(bg="lightgray")
        root.state('zoomed')
        title = tk.Label(root, text="Circuit Simulator", font = ("Inter", 40), bg = "lightgray")
        title.pack(pady=75)
        enter = tk.Button(root, text="Open Canvas", font = ("IBM Plex Sans", 20), bg = "gray")
        enter.configure(command = lambda: self.openCanvas(root))
        enter.pack(pady = 100)
        root.mainloop()

    def openCanvas(self, root) -> None:
        self.canvas.openCanvas(root)
    