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


        # Additional Imports Frame
        self.importFrame = tk.LabelFrame(self, text='Additional Imports')

        # Window Dimension Frame
        self.dimensionFrame = tk.LabelFrame(self, text="Window Dimension")

        # Window Title Frame
        self.titleFrame = tk.LabelFrame(self, text="Window Title")

        # File Destination Frame
        self.destinationFrame = tk.LabelFrame(self, text="Select File Destination")

        # Create Button
        self.create = tk.Button(self, text="Create")

        # Frames Grids
        self.nameFrame.grid(row=0, column=0)
        self.importFrame.grid(row=1, column=0)
        self.dimensionFrame.grid(row=2, column=0)
        self.titleFrame.grid(row=3, column=0)
        self.destinationFrame.grid(row=4, column=0)
        self.create.grid(row=5, column=0)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
