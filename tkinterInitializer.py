import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        self.label = tk.Label(self, text="This is a label")
        self.label.grid()

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()