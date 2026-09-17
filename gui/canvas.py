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
        self.ammeter = tk.PhotoImage(file = "assets/ammeter.png").subsample(10, 10)
        self.voltmeter = tk.PhotoImage(file = "assets/voltmeter.png").subsample(10, 10)
        self.vresistor = tk.PhotoImage(file = "assets/vresistor.png").subsample(15, 15)
        self.thermistor = tk.PhotoImage(file = "assets/thermistor.png").subsample(10, 10)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        optionsBox = tk.Frame(self, bg = "lightgray")
        optionsBox.grid(row=0, column=0, columnspan = 3, sticky = "ew", padx = 10, pady = 10)

        optionsButtonStyle = ttk.Style()
        optionsButtonStyle.configure("TButton", font=("IBM Plex Sans", 20), padding=10, background = "#4A4A4A", foreground = "black")

        
        back = ttk.Button(optionsBox, text="Back ↩", style="TButton", command=self.gui.showMainMenu)
        back.grid(row=0, column=0, columnspan = 1, sticky = "w")

        componentsBox = tk.Frame(self, bg = "lightgray")
        componentsBox.grid(row=1, column=2, sticky = "ns", padx = 10, pady = 10)

        canvas = tk.Canvas(self, bg="white")
        canvas.grid(row=1, column = 1, sticky = "nsew", padx = 10, pady = 10)

        resistorComponent = tk.Label(componentsBox, image = self.resistor, compound = "top", text = "Resistor", font = ("IBM Plex Sans", 10), bg = "lightgray")
        resistorComponent.grid(row=0, column=0, padx = 10, pady = 10)
        resistorComponent.bind("<Enter>", lambda e: self.highlight(e))
        resistorComponent.bind("<Leave>", lambda e: self.unhighlight(e))

        lampComponent = tk.Label(componentsBox, image = self.lamp, compound = "top", text = "Lamp", font = ("IBM Plex Sans", 10), bg = "lightgray")
        lampComponent.grid(row=1, column=0, padx = 10, pady = 10)
        lampComponent.bind("<Enter>", lambda e: self.highlight(e))
        lampComponent.bind("<Leave>", lambda e: self.unhighlight(e))

        ammeterComponent = tk.Label(componentsBox, image = self.ammeter, compound = "top", text = "Ammeter", font = ("IBM Plex Sans", 10), bg = "lightgray")
        ammeterComponent.grid(row=2, column=0, padx = 10, pady = 10)
        ammeterComponent.bind("<Enter>", lambda e: self.highlight(e))
        ammeterComponent.bind("<Leave>", lambda e: self.unhighlight(e))
        voltmeterComponent = tk.Label(componentsBox, image = self.voltmeter, compound = "top", text = "Voltmeter", font = ("IBM Plex Sans", 10), bg = "lightgray")
        voltmeterComponent.grid(row=3, column=0, padx = 10, pady = 10)
        voltmeterComponent.bind("<Enter>", lambda e: self.highlight(e))
        voltmeterComponent.bind("<Leave>", lambda e: self.unhighlight(e))

        vresistorComponent = tk.Label(componentsBox, image = self.vresistor, compound = "top", text = "Variable Resistor", font = ("IBM Plex Sans", 10), bg = "lightgray")
        vresistorComponent.grid(row=4, column=0, padx = 10, pady = 10)
        vresistorComponent.bind("<Enter>", lambda e: self.highlight(e))   
        vresistorComponent.bind("<Leave>", lambda e: self.unhighlight(e))

        thermistorComponent = tk.Label(componentsBox, image = self.thermistor, compound = "top", text = "Thermistor", font = ("IBM Plex Sans", 10), bg = "lightgray")
        thermistorComponent.grid(row=5, column=0, padx = 10, pady = 10)
        thermistorComponent.bind("<Enter>", lambda e: self.highlight(e))
        thermistorComponent.bind("<Leave>", lambda e: self.unhighlight(e))

    def highlight(self, event) -> None:
        event.widget.configure(bg = "#B3AAAA", borderwidth = 1, relief = "solid")
    def unhighlight(self, event) -> None:
        event.widget.configure(bg = "lightgray", borderwidth = 0, relief = "flat")