import tkinter as tk
from tkinter import ttk
from gui import canvas
from circuit import Circuit


class MainGUI:

    def __init__(self) -> None:
        #creates the main window as a tkinter instance
        self.root = tk.Tk()

        #sets up the basic settings of the GUI
        self.root.title("CircuitSim")
        self.root.geometry("500x500")
        self.root.configure(bg="lightgray")

        #auto maximises the window when the program runs
        self.root.state("zoomed")

        #creates a "frame" for the Startup GUI
        self.main = tk.Frame(self.root, bg="lightgray")
        #creates a "frame" for the circuit building canvas GUI
        self.circuit = Circuit("Untitled")
        self.canvas = canvas.Canvas(self.root, self)

        #places the frames in the main window we opened, root
        self.main.place(relheight=1, relwidth=1)
        self.canvas.place(relheight=1, relwidth=1)

        #sets up the startup gui, and then "raises" to the top
        self.buildMainMenu()
        self.showMainMenu()

    def buildMainMenu(self) -> None:

        #adds a title as a text label, on the top of the screen.
        #uses the pack method for now, to place the title label in the centre, with only y axis padding.
        title = tk.Label(self.main, text="Circuit Simulator", font=("IBM Plex Sans", 40), bg="lightgray")
        title.pack(pady=50)

        #uses ttk to create a button style, which can be configured and then applied to buttons.
        buttonStyle = ttk.Style()

        #configuring the button style
        buttonStyle.configure("TButton", font=("IBM Plex Sans", 20), padding=10, background = "#4A4A4A", foreground = "black")

        #creates the necessary ttk buttons, applies the button style, and then places
        start = ttk.Button(self.main, text="Open Canvas", style="TButton", command=self.showCanvas)
        start.pack(pady=20)
        quit = ttk.Button(self.main, text="Quit", style="TButton", command=self.root.quit)
        quit.pack(pady=20)


    def showMainMenu(self) -> None:
        self.root.title("CircuitSim")
        self.main.tkraise()

    def showCanvas(self) -> None:
        self.root.title("Circuit Canvas")
        self.canvas.tkraise()
        

    def setupWindow(self) -> None:
        self.root.mainloop()