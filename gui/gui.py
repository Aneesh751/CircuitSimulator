import tkinter as tk



class MainGUI:



    def openWindow(self) -> None:
        root = tk.Tk()
        root.title("CircuitSim")
        root.geometry("500x500")
        root.configure(bg="lightgray")
        
        root.mainloop()
