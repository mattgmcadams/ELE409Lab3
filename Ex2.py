from tkinter import *
from sense_hat import SenseHat
sense = SenseHat()

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title