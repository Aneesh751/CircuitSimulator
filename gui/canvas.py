import tkinter as tk


class Canvas(tk.Frame):

    def __init__(self, parent, gui) -> None:
        super().__init__(parent, bg="lightblue")
        self.gui = gui
        self.createCanvas()

    def createCanvas(self) -> None:

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

        exampleComponent = tk.Button(componentsBox, text="Example Component", font=("IBM Plex Sans", 15), bg="gray")
        exampleComponent.grid(row=0, column=0, padx = 10, pady = 10)