import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.inputFrame = tk.LabelFrame(self)

        # File Name
        self.nameLabel = tk.Label(self.inputFrame, text="Enter the name of your python file: ")
        self.fileName = tk.Text(self.inputFrame, height=1, width=35)  # I prefer Text than Entry

        # Additional Imports
        self.importLabel = tk.Label(self.inputFrame, text="[Optional] Enter additional imports \n(Random,String, etc..,"
                                                          " separated with spaces)")
        self.additionalImports = tk.Text(self.inputFrame, height=1, width=35)
        self.i = tk.IntVar()
        self.noImports = tk.Radiobutton(self.inputFrame, text="Continue without imports", value=1, variable=self.i,
                                        command=lambda: self.no_imports(self.i.get()))
        # Window Dimension
        self.dimensionLabel = tk.Label(self.inputFrame, text="Enter the dimension for your window\n Default: 300x300, "
                                                             "use the Default format for your input", padx=5)
        self.dimension = tk.Text(self.inputFrame, height=1, width=35)
        self.d = tk.IntVar()  # Default dimension variable
        self.defaultDimension = tk.Radiobutton(self.inputFrame, text="Use Default", value=2, variable=self.d,
                                               command=lambda: self.use_default(self.d.get()))
        # Window Title
        self.titleLabel = tk.Label(self.inputFrame, text="Enter the title of your window:")
        self.title = tk.Text(self.inputFrame, width=35, height=1)

        # File Destination
        self.destinationlabel = tk.Label(self.inputFrame, text="Choose File Destination")
        self.fileDestination = tk.Text(self.inputFrame, width=35, height=1)
        self.chooseBtn = tk.Button(self.inputFrame, text="...", command=self.choose_destination, pady=1)

        # Create Button
        self.create = tk.Button(self, text="Create", pady=5)

        # Grids
        self.nameLabel.grid(row=0, column=0, columnspan=3)
        self.fileName.grid(row=1, column=1)
        tk.Label(self.inputFrame).grid(row=2)
        self.importLabel.grid(row=3, column=0, columnspan=3)
        self.additionalImports.grid(row=4, column=1)
        self.noImports.grid(row=5, column=1)
        tk.Label(self.inputFrame).grid(row=6)
        self.dimensionLabel.grid(row=7, column=0, columnspan=3)
        self.dimension.grid(row=8, column=1)
        self.defaultDimension.grid(row=9, column=1)
        tk.Label(self.inputFrame).grid(row=10)
        self.titleLabel.grid(row=11, column=0, columnspan=3)
        self.title.grid(row=12, column=1)
        tk.Label(self.inputFrame).grid(row=13)
        self.destinationlabel.grid(row=14, column=0, columnspan=3)
        self.fileDestination.grid(row=15, column=1)
        self.chooseBtn.grid(row=15, column=2)

        # Frame Grid
        self.inputFrame.grid(row=0, column=0, columnspan=4, padx=5)
        self.create.grid(row=1, column=3, pady=10)

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
