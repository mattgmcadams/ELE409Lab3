from tkinter import *
import numpy as np
from sense_hat import SenseHat
sense=SenseHat()

sense.clear()

R = (255, 0, 0)
a = np.zeros([8,8])
p = np.zeros([64,1])

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("LED Controller and Monitor")
        self.geometry("300x300")
        self.buttons = {}
        for x in range(8):
            for y in range(8):
                handler = lambda x=x, y=y: self.led(x, y)
                self.button = Button(self, command=handler,
                                     width=1, height=1, activebackground='#d9d9d9')
                self.button.grid(row=y, column=x)
                self.buttons[x, y] = self.button
        self.clear = Button(self, text="Reset",
                            command=self.clear)
        self.clear.grid(row=8, column=3, columnspan=2)
        self.readpixel()

    def led(self, x, y):
        global a
        if a[x, y] == 0:
            sense.set_pixel(x, y, R)
            self.buttons[x, y].config(bg='red',
                                      activebackground='red')
            a[x, y] = 1
        else:
            sense.set_pixel(x, y, (0, 0, 0))
            self.buttons[x, y].config(bg='#d9d9d9',
                                      activebackground='#d9d9d9')
            a[x,y] = 0


    def readpixel(self):
        global p
        pixels = sense.get_pixels()
        for i in range(64):
            if pixels[i] != [0, 0, 0]:
                p[i] = 1
        else:
            p[i] = 1
        pixel = p.reshape(8, 8)
        for x in range(8):
            for y in range(8):
                if pixel[x, y] == 1:
                    self.buttons[y, x].config(bg='red',
                                              activebackground='red')
                else:
                    self.buttons[y, x].config(bg='#d9d9d9',
                                              activebackground='#d9d9d9')
        self.after(300, self.readpixel)

    def clear(self):
        global a
        a = np.zeros([8,8])
        for x in range(8):
            for y in range(8):
                self.buttons[x,y].config(bg='#d9d9d9', activebackground='#d9d9d9')
        sense.clear()

root = Root()
root.mainloop()