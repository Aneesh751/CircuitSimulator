import tkinter as tk
from tkinter import ttk


class Canvas(tk.Frame):



    def __init__(self, parent, gui) -> None:
        super().__init__(parent, bg="lightblue")
        self.gui = gui
        self.createCanvas()

    def createCanvas(self) -> None:
        self.resistor = tk.PhotoImage(file="assets/resistor.png").subsample(15, 15)
        self.lamp = tk.PhotoImage(file = "assets/lamp.png").subsample(10, 10)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        optionsBox = tk.Frame(self, bg = "lightgray")
        optionsBox.grid(row=0, column=0, columnspan = 3, sticky = "ew", padx = 10, pady = 10)
        
        back = tk.Button(optionsBox, text="Back to Main Menu", font=("IBM Plex Sans", 20), bg="gray", command=self.gui.showMainMenu)
        back.grid(row=0, column=0, columnspan = 1, sticky = "w")

        componentsBox = tk.Frame(self, bg = "lightgray")
        componentsBox.grid(row=1, column=2, sticky = "ns", padx = 10, pady = 10)

        canvas = tk.Canvas(self, bg="white")
        canvas.grid(row=1, column = 1, sticky = "nsew", padx = 10, pady = 10)

        resistorComponent = tk.Label(componentsBox, image = self.resistor, compound = "top", text = "Resistor", font = ("IBM Plex Sans", 10), bg = "lightgray")
        resistorComponent.grid(row=0, column=0, padx = 10, pady = 10)
        lampComponent = tk.Label(componentsBox, image = self.lamp, compound = "top", text = "Lamp", font = ("IBM Plex Sans", 10), bg = "lightgray")
        lampComponent.grid(row=1, column=0, padx = 10, pady = 10)