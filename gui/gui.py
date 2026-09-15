import tkinter as tk



class MainGUI:

    def openWindow(self) -> None:
        root = tk.Tk()
        root.title("CircuitSim")
        root.geometry("500x500")
        root.configure(bg="lightgray")
        tk.Label(root, text="Test text", font=("Arial", 16), bg="lightblue").pack(pady=250)
        root.mainloop()