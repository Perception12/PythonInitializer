import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        # File Name Frame
        self.nameFrame = tk.LabelFrame(self, text='File Name')
        self.nameLabel = tk.Label(self.nameFrame, text="Enter the name of your python file: ", padx=15, pady=10)
        self.fileName = tk.Text(self.nameFrame, height=1, width=35)  # I prefer Text than Entry

        # File name grids
        self.nameLabel.grid(row=0, column=0)
        self.fileName.grid(row=1, column=0)

        # Additional Imports Frame
        self.importFrame = tk.LabelFrame(self, text='Additional Imports')

        self.importLabel = tk.Label(self.importFrame, text="[Optional] Enter additional imports \n" +
                                                           "(Random,String, etc.., separated with spaces)")

        self.additionalImports = tk.Text(self.importFrame, height=1, width=35)
        self.i = tk.IntVar()
        self.noImports = tk.Radiobutton(self.importFrame, text="Continue without imports", value=1, variable=self.i,
                                        command=lambda: self.no_imports(self.i.get()))

        # Additional Imports grids
        self.importLabel.grid(row=0, column=0)
        self.additionalImports.grid(row=1, column=0)
        self.noImports.grid(row=2, column=0)

        # Window Dimension Frame
        self.dimensionFrame = tk.LabelFrame(self, text="Window Dimension")
        self.dimensionLabel = tk.Label(self.dimensionFrame, text="Enter the dimension for your window\n"
                                                                 "Default: 300x300, use the Default format for your "
                                                                 "input")
        self.dimension = tk.Text(self.dimensionFrame, height=1, width=35)
        self.d = tk.IntVar() # Default dimension variable
        self.defaultDimension = tk.Radiobutton(self.dimensionFrame, text="Use Default", value=2, variable=self.d,
                                               command=lambda: self.use_default(self.d.get()))

            # Dimension Frame Grids
        self.dimensionLabel.grid(row=0, column=0)
        self.dimension.grid(row=1, column=0)
        self.defaultDimension.grid(row=2, column=0)

        # Window Title Frame
        self.titleFrame = tk.LabelFrame(self, text="Window Title")
        self.titleLabel = tk.Label(self.titleFrame, text="Enter the title of your window:")
        self.title = tk.Text(self.titleFrame, width=35, height=1)

            # Window Title Grids
        self.titleLabel.grid(row=0, column=0)
        self.title.grid(row=1, column=0)

        # File Destination Frame
        self.destinationFrame = tk.LabelFrame(self, text="Destination")
        self.destinationlabel = tk.Label(self.destinationFrame, text="Choose File Destination")
        self.fileDestination = tk.Text(self.destinationFrame, width=35, height=1)
        self.chooseBtn = tk.Button(self.destinationFrame, text="...", command=self.choose_destination)

            # Destination Grids
        self.destinationlabel.grid(row=0, column=0)
        self.fileDestination.grid(row=1, column=0)
        self.chooseBtn.grid(row=1, column=1)

        # Create Button
        self.create = tk.Button(self, text="Create")

        # Frames Grids
        self.nameFrame.grid(row=0, column=0)
        self.importFrame.grid(row=1, column=0)
        self.dimensionFrame.grid(row=2, column=0)
        self.titleFrame.grid(row=3, column=0)
        self.destinationFrame.grid(row=4, column=0)
        self.create.grid(row=5, column=0)

    def no_imports(self, value):
        pass

    def use_default(self, value):
        pass

    def choose_destination(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Tkinter Initializer")
    app = Application(root)
    app.mainloop()
