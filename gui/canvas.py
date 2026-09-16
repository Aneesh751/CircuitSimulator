from tkinter import ttk
import tkinter as tk
from gui import gui

class Canvas:

    def __init__(self) -> None:
        pass

    def openCanvas(self, root) -> None:
        root.destroy()
        canvas = tk.Tk()
        canvas.title("Circuit Canvas")
        canvas.geometry("1000x1000")
        canvas.configure(bg="lightblue")
        canvas.state('zoomed')
        back = tk.Button(canvas, text="Back to main menu", font = ("IBM Plex Sans", 20), bg = "gray")
        back.configure(command = lambda: self.returnToMenu(canvas))
        back.grid(row = 0, column = 0, padx = 10, pady = 10)
        canvas.mainloop()

    def returnToMenu(self, canvas) -> None:
        canvas.destroy()
        self.gui = gui.MainGUI()
        self.gui.openWindow()