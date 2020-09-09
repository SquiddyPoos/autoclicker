from tkinter import *
from autoclicker import Autoclicker, AutoclickError

class App(object):

    def __init__(self):
        self.root = Tk()
        self.autoclicker = Autoclicker()
        self.setup_gui()
        self.root.mainloop()

    def setup_gui(self):
        pass