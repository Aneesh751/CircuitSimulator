import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from gui import canvas
from circuit import Circuit


class MainGUI:
    def __init__(self) -> None:

        #colours and gradients
        self.bgColour = "#F3F6F9"
        self.pColour = "#19354D"
        self.sColour = "#64748B"
        self.accent = "#294F70"
        self.borderColour = "#9CB5C9"
        self.tint = "#DCE8F1"

        

        #creates the main window as a tkinter instance. this is what the whole window will be based off of
        self.root = tk.Tk()
        #sets up the basic settings of the gui, like the title of the window, how big it is and the background
        self.root.title("CircuitSim")
        self.root.geometry("500x500")
        self.root.configure(bg = self.bgColour)


        #auto maximises the window when the program runs, so its fullscreen
        self.root.state("zoomed")

        #util images
        self.bg = tk.PhotoImage(file = "assets/bg.png")

        #creates a "frame" for the startup gui, which can be "raised" or "lowered" to switch between windows smoothly
        self.main = tk.Frame(self.root, bg = self.bgColour)
        #creates a "frame" for the circuit building canvas GUI
        self.circuit = Circuit("Untitled")
        self.canvas = canvas.Canvas(self.root, self)

        #places the frames in the main window we opened, root
        self.main.place(relheight = 1, relwidth = 1)
        self.canvas.place(relheight = 1, relwidth = 1)

        #background
        self.mainbg = tk.Label(self.main, image = self.bg, bg = self.bgColour)
        self.mainbg.place(relx = 1, rely = 0, anchor = "ne")
        #sets up the startup gui, and then "raises" to the top
        self.buildMainMenu()
        self.showMainMenu()

    def buildMainMenu(self) -> None:

        #adds a title as a text label, on the top of the screen.
        #uses the pack method for now, to place the title label in the centre, with only y axis padding.
        title = tk.Label(self.main, text = "Circuit Simulator v1.2", font = ("IBM Plex Sans", 40), bg = self.bgColour, fg = self.pColour)
        title.pack(pady = (120, 15))
        subtitle = tk.Label(self.main, text = "Open Canvas to get started", font = ("IBM Plex Sans", 20), bg = self.bgColour, fg = self.sColour)
        subtitle.pack(pady = 5)

        #uses ttk to create a button style, which can be configured and then applied to buttons.
        buttonStyle = ttk.Style()



        #configuring the button style for the open canvas button
        buttonStyle.configure("TButton", font = ("IBM Plex Sans", 15), padding = 10)
        #creates the necessary ttk buttons, applies the button style, and then places
        start = ctk.CTkButton(self.main, text = "Open Canvas", command = self.showCanvas, width = 22, height = 40, fg_color = self.pColour, hover_color = self.accent, text_color = "white", font = ("IBM Plex Sans", 15))
        start.pack(pady = (0, 12))
        quit = ttk.Button(self.main, text = "Quit", style = "TButton", command = self.root.quit, width = 22)
        quit.pack()


    def showMainMenu(self) -> None:
        self.root.title("CircuitSim")
        self.main.tkraise()
    def showCanvas(self) -> None:
        self.root.title("Circuit Canvas")
        self.canvas.tkraise()

    def setupWindow(self) -> None:
        self.root.mainloop()