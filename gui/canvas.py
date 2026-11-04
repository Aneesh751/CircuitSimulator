import tkinter as tk
from tkinter import ttk
from components import Component

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

        #utility button images
        self.delete = tk.PhotoImage(file = "assets/delete.png").subsample(7, 7)
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

        #separate frames for options, components, canvas and navigation buttons
        optionsBox = tk.Frame(self, bg = "lightgray")
        optionsBox.grid(row=0, column=0, columnspan = 3, sticky = "ew", padx = 10, pady = 10)
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

        #panel that opens up for a component on the canvas
        self.sidePanel = tk.Frame(self.componentsBox, bg = "white", padx = 10, pady = 10)
        self.sidePanel.grid(row = 2, column = 0, sticky = "ew", pady = 10)
        #hide the panel so that it doesnt always show whenever the canvas gui opens
        self.sidePanel.grid_remove()
        self.detailsLabel = tk.Label(self.sidePanel, bg = "white", font = ("IBM Plex Sans", 12), image = self.delete, compound = "bottom")
        self.detailsLabel.bind("<Button-1>", self.deleteComponent)
        self.detailsLabel.configure(text = "")
        
        self.detailsLabel.pack(side = "left", padx = 5)

    

        optionsButtonStyle = ttk.Style()
        optionsButtonStyle.configure("TButton", font=("IBM Plex Sans", 20), padding=10, background = "#4A4A4A", foreground = "black")
        self.previous = ttk.Button(self.navigationFrame, text = "Previous", style = "TButton", command = self.previousPage)
        self.previous.grid(row=2, column=0, padx = 5, pady = 5)
        self.next = ttk.Button(self.navigationFrame, text= "Next", style = "TButton", command=self.nextPage)
        self.next.grid(row=0, column=0, padx = 5, pady=5)
        self.pLabel = tk.Label(self.navigationFrame, text="1/1", bg="lightgray")
        self.pLabel.grid(row = 1, column = 0, padx=5, pady = 5)
        back = ttk.Button(optionsBox, text = "Back ↩", style =  "TButton", command = self.gui.showMainMenu)
        back.grid(row=0, column=0, columnspan = 1, sticky = "w")
        clear = ttk.Button(optionsBox, text = "Clear Canvas", style = "TButton", command = self.clearCanvas)
        clear.grid(row = 0, column = 1, columnspan = 1, sticky = "e")

    
        #the actual canvas where components can be placed
        self.drawingCanvas = tk.Canvas(self, bg="white")
        self.drawingCanvas.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        #mouse events
        self.drawingCanvas.bind("<Button-1>", self.selectAndDrag)
        self.drawingCanvas.bind("<B1-Motion>", self.dragSelected)
        self.drawingCanvas.bind("<ButtonRelease-1>", self.releaseSelected)

        #delete key
        self.gui.root.bind("<Delete>", self.deleteComponent)
        #dictionary to keep track of components that are placed
        self.placedComponents: dict[int, Component] = {}
        #id to identify a component on the canvas being selected
        self.selectedItemID : int | None = None
        #offset of a drag
        self.dragOffset: tuple[int, int] | None = None


        #dictionary to store components with the name as keys
        self.componentImages = dict(components)
        #variables to keep track
        self._drag = None
        self._dragStart = None
        self._dragged = False
        self._previewId = None

        for name, image in components:
            component = tk.Label(componentsContainer, image = image, compound= "top", text = name, font = ("IBM Plex Sans", 10) , bg= "lightgray")
            component.bind("<Enter>", lambda event: self.highlight(event))
            component.bind("<Leave>", lambda event: self.unhighlight(event))
            component.bind("<ButtonPress-1>", lambda event, n=name, img=image: self.startDrag(event, n, img))
            component.bind("<B1-Motion>", self.dragMotion)
            component.bind("<ButtonRelease-1>", self.dropComponent)
            self.items.append(component)

        self.componentsBox.bind("<Configure>", self.handleComponentsResize)
        self.after_idle(self.calculateItemsPerPage)
    def selectAndDrag(self, event) -> None:
        #this gets the components currently under the mouse pointer that have been placed on the canvas
        currentComponents = self.drawingCanvas.find_withtag("current")

        if not currentComponents:
            self.cancelSelection()
            return
        itemId = currentComponents[-1]
        if itemId not in self.placedComponents:
            self.cancelSelection()
            return
        self.selectedItemID = itemId
        component = self.placedComponents[itemId]
        self.detailsLabel.configure(text = component.name)
        self.sidePanel.grid()
        x_cord = self.drawingCanvas.canvasx(event.x)
        y_cord = self.drawingCanvas.canvasy(event.y)
        image_x, image_y = self.drawingCanvas.coords(itemId)

        #this saves the deviation between the actual click position and the position of the image, so dragging is smooth
        self.dragOffset = (x_cord - image_x, y_cord - image_y)
    def dragSelected(self, event) -> None:
        #checks to cancel the method if nothing valid has been selected or if the component hasnt been dragged
        if self.selectedItemID is None: 
            return
        if self.dragOffset is None:
            return
        origX = self.drawingCanvas.canvasx(event.x)
        origY = self.drawingCanvas.canvasy(event.y)
        newX = origX - self.dragOffset[0]
        newY = origY - self.dragOffset[1]
        self.drawingCanvas.coords(self.selectedItemID, newX, newY)

        component = self.placedComponents[self.selectedItemID]
        component.x = round(newX)
        component.y = round(newY)
        #rounding to make sure the new coordinates are integers, because the components class needs integers
    def releaseSelected(self, event) -> None:
        self.dragOffset = None

    def deleteComponent(self, event = None) -> None:
        if self.selectedItemID is None:
            return

        #this method is called whenever the delete key is pressed, so there needs to be a way to prevent a component
        #being deleted if the user is typing something in a text box, not necessarily deleting a component.
        #to do this i'll check which "element" is currently in focus by the keyboard.
        focusedElement = self.gui.root.focus_get()
        #this checks if the element in focus by the keyboard is a text entry or not.
        if isinstance(focusedElement, (tk.Entry, ttk.Entry)):
            return
        #if not, proceed as normal#
        component = self.placedComponents.pop(self.selectedItemID)
        self.drawingCanvas.delete(self.selectedItemID)
        self.gui.circuit.remove_component(component)
        self.cancelSelection()

        return "break"
    def cancelSelection(self) -> None:
        self.selectedItemID = None
        self.dragOffset = None
        self.sidePanel.grid_remove()



    def clearCanvas(self) -> None:
        self.drawingCanvas.delete("all")
        self.gui.circuit.clear_components()
        self.placedComponents.clear()
        self.cancelSelection()
    def startDrag(self, event, name: str, image) ->  None:
        self._drag = {"name": name, "image": image}
        self._dragStart = (event.x_root, event.y_root)
        self._dragged = False
    def relcanvasPosition(self, event) -> tuple[int, int, bool]:
        x = event.x_root - self.drawingCanvas.winfo_rootx()
        y = event.y_root - self.drawingCanvas.winfo_rooty()
        inside = (0 <= x < self.drawingCanvas.winfo_width()) and (0 <= y < self.drawingCanvas.winfo_height() )
        return x, y, inside
    
    def dragMotion(self, event) -> None:
        if self._drag is None:
            return
        startX, startY = self._dragStart
        if not self._dragged:

            #this will ignore very small cursor movements
            if max(abs(event.x_root - startX), abs(event.y_root - startY)) < 4:
                return
            #if not its being dragged
            self._dragged = True
        x, y, inside = self.relcanvasPosition(event)
        if not inside:
            if self._previewId is not None:
                self.drawingCanvas.delete(self._previewId)
                self._previewId = None
            return
        if self._previewId is None:
            self._previewId = self.drawingCanvas.create_image(x, y, image = self._drag["image"])
        else:
            self.drawingCanvas.coords(self._previewId, x, y)

    def dropComponent(self, event) -> None:
        if self._drag is None:
            return
        drag = self._drag
        x, y, inside = self.relcanvasPosition(event)
        if self._previewId is not None:
            self.drawingCanvas.delete(self._previewId)
            self._previewId = None
        self._drag = None
        self._dragStart = None
        if self._dragged and inside:
            placed = Component(drag["name"], x, y)
            self.gui.circuit.add_component(placed)

            item_id = self.drawingCanvas.create_image(x, y, image=self.componentImages[placed.name])   
            self.placedComponents[item_id] = placed

    def handleComponentsResize(self, event = None) -> None:
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
    



