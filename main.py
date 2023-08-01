import os
from tkinter import Tk
import gui

class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        gui.gui(self)
        self.mainloop()

if __name__ == "__main__":
    App()