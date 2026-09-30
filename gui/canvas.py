import tkinter as tk
from tkinter import ttk


class Canvas(tk.Frame):



    def __init__(self, parent, gui) -> None:
        super().__init__(parent, bg="lightblue")
        self.gui = gui
        self.createCanvas()

    def createCanvas(self) -> None:

        #images for components
        self.resistor = tk.PhotoImage(file="assets/resistor.png").subsample(15, 15)
        self.lamp = tk.PhotoImage(file = "assets/lamp.png").subsample(10, 10)
        self.ammeter = tk.PhotoImage(file = "assets/ammeter.png").subsample(10, 10)
        self.voltmeter = tk.PhotoImage(file = "assets/voltmeter.png").subsample(10, 10)
        self.vresistor = tk.PhotoImage(file = "assets/vresistor.png").subsample(15, 15)
        self.thermistor = tk.PhotoImage(file = "assets/thermistor.png").subsample(10, 10)
        self.cell = tk.PhotoImage(file = "assets/cell.png").subsample(10, 10)
        self.battery = tk.PhotoImage(file = "assets/battery.png").subsample(10, 10)
        self.diode = tk.PhotoImage(file = "assets/diode.png").subsample(10, 10)
        self.switch = tk.PhotoImage(file = "assets/switch.png").subsample(10,10)
        self.fuse = tk.PhotoImage(file = "assets/fuse.png").subsample(10,10)
        self.led = tk.PhotoImage(file = "assets/led.png").subsample(10, 10)
        self.ldr = tk.PhotoImage(file = "assets/ldr.png").subsample(7, 7)


        #the array containing all the components

        components = [
            ("Resistor", self.resistor),
            ("Lamp", self.lamp),
            ("Ammeter", self.ammeter),
            ("Voltmeter", self.voltmeter),
            ("Variable Resistor", self.vresistor),
            ("Thermistor", self.thermistor),
            ("Cell", self.cell),
            ("Battery", self.battery),
            ("Diode", self.diode),
            ("Switch", self.switch),
            ("Fuse", self.fuse),
            ("LED", self.led),
            ("LDR", self.ldr),
        ]

        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight = 0)
        self.currentPage = 0
        self.itemsPerPage = 0
        self.items = []
        self.resizeJob = None

        #options toolbar at the top
        optionsBox = tk.Frame(self, bg = "lightgray")
        optionsBox.grid(row=0, column=0, columnspan = 3, sticky = "ew", padx = 10, pady = 10)

        optionsButtonStyle = ttk.Style()
        optionsButtonStyle.configure("TButton", font=("IBM Plex Sans", 20), padding=10, background = "#4A4A4A", foreground = "black")

        #buttons
        back = ttk.Button(optionsBox, text="Back ↩", style="TButton", command=self.gui.showMainMenu)
        back.grid(row=0, column=0, columnspan = 1, sticky = "w")




        #the frames
        self.componentsBox = tk.Frame(self, bg = "lightgray")
        self.componentsBox.grid(row=1, column=2, sticky = "nsew", padx = 10, pady = 10)
        self.componentsBox.columnconfigure(0, weight=1)
        self.componentsBox.rowconfigure(0, weight=1)
        componentsContainer = tk.Frame(self.componentsBox, bg = "lightgray")
        componentsContainer.grid(row=0, column = 0, sticky = "nsew")
        componentsContainer.columnconfigure(0, weight=1)
        self.navigationFrame = tk.Frame(self.componentsBox, bg = "lightgray")
        self.navigationFrame.grid(row=1, column = 0, sticky = "ew")
        self.navigationFrame.columnconfigure(0, weight=0)

        self.previous = ttk.Button(self.navigationFrame, text="Previous", style="TButton", command=self.previousPage)
        self.previous.grid(row=2, column=0, padx = 5, pady = 5)
        self.next = ttk.Button(self.navigationFrame, text="Next", style="TButton", command=self.nextPage)
        self.next.grid(row=0, column=0, padx = 5, pady=5)
        self.pLabel = tk.Label(self.navigationFrame, text="1/1", bg="lightgray")
        self.pLabel.grid(row = 1, column = 0, padx=5, pady = 5)

    

        canvas = tk.Canvas(self, bg="white")
        canvas.grid(row=1, column = 1, sticky = "nsew", padx = 10, pady = 10)

        for name, image in components:
            component = tk.Label(componentsContainer, image=image, compound = "top", text = name, font = ("IBM Plex Sans", 10), bg = "lightgray")
            component.bind("<Enter>", lambda e: self.highlight(e))
            component.bind("<Leave>", lambda e: self.unhighlight(e))
            self.items.append(component)


        self.componentsBox.bind("<Configure>", self.handleComponentsResize)
        self.after_idle(self.calculateItemsPerPage)

    def handleComponentsResize(self, event=None) -> None:
        if self.resizeJob is not None:
            self.after_cancel(self.resizeJob)

        self.resizeJob = self.after(100, self.calculateItemsPerPage)

    def highlight(self, event) -> None:
        event.widget.configure(bg = "#B3AAAA", borderwidth = 1, relief = "solid")
    def unhighlight(self, event) -> None:
        event.widget.configure(bg = "lightgray", borderwidth = 0, relief = "flat")

    def calculateItemsPerPage(self) -> None:
        self.update_idletasks()

        availableHeight = self.componentsBox.winfo_height()
        navigationHeight = self.navigationFrame.winfo_reqheight()
        possibleHeight = availableHeight - navigationHeight - 5

        if possibleHeight <= 0:
            return
        
        itemHeights = [
            component.winfo_reqheight()
            for component in self.items
        ]
        if not itemHeights:
            return
        itemHeight = max(itemHeights) - 25
        itemPerPage = max(1, possibleHeight // itemHeight)

        if itemPerPage != self.itemsPerPage:
            self.itemsPerPage = itemPerPage
            totalPages = self.getTotalPages()
            if self.currentPage >= totalPages:
                self.currentPage = totalPages - 1
            self.showCurrentPage()

    def getTotalPages(self) -> int:
        if self.itemsPerPage <= 0:
            return 1
        return max(1, (len(self.items) + self.itemsPerPage - 1) // self.itemsPerPage)

    def showCurrentPage(self) -> None:
        for item in self.items:
            item.grid_remove()

        sIndex = self.currentPage * self.itemsPerPage
        eIndex = sIndex + self.itemsPerPage

        viewableItems = self.items[sIndex:eIndex]

        for row, item in enumerate(viewableItems):
            item.grid(row = row, column = 0, padx = 10, pady = 10)
        totalPages = self.getTotalPages()

        self.pLabel.configure(text=f"{self.currentPage + 1} / {totalPages}")

        self.previous.configure(state = "normal" if self.currentPage > 0 else "disabled")
        self.next.configure(state = "normal" if self.currentPage < totalPages - 1 else "disabled")

        if totalPages <= 1:
            self.navigationFrame.grid_remove()
        else:
            self.navigationFrame.grid()

    def previousPage(self) -> None:
        if self.currentPage > 0:
            self.currentPage -= 1
            self.showCurrentPage()

    def nextPage(self) -> None:
        if self.currentPage < self.getTotalPages() - 1:
            self.currentPage += 1
            self.showCurrentPage()
    



