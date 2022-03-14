from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sense_hat import SenseHat
sense = SenseHat()

# Create figure for plotting
f = plt.figure()
ax = f.add_subplot(1, 1, 1)
xs = []
ys = []

class getData(object):
    def getGaussian(self): return np.random.normal()
    def getTemperature(self): return sense.get_temperature()
    def getTime(self): return dt.datetime.now().strftime('%H:%M:%S')

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.display_chart = False
        
        self.title("Tkinter Embedding Matplotlib")
        self.geometry("600x500")
        self.gaussian = getData()
        self.button1 = Button(self, text="Display",
                              command=self.display)
        self.button1.grid(row=0, column=0, padx=50)
        self.canvas = FigureCanvasTkAgg(f, self)
        # self.canvas.get_tk_widget().grid(row=1, column=0, pady=10)

    def update_fig(self):
        global xs, ys
        g = self.gaussian.getTemperature()
        t = self.gaussian.getTime()
        # Add time and gaussian value to lists
        xs.append(t)
        ys.append(g)
        #limit x and y to 10 items
        xs = xs[-10:]
        ys = ys[-10:]

        ax.clear()
        ax.plot(xs, ys)

        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=.30)
        plt.title('Temperature Variation')
        plt.ylabel('Temperature')
        plt.ylim((30, 40))
        self.canvas.draw()
        if self.display_chart:
            self.after(1000, self.update_fig)

    def display(self):
        self.display_chart = True
        self.canvas = FigureCanvasTkAgg(f, self)
        self.canvas.get_tk_widget().grid(row=1, column=0, pady=10, columnspan=10)
        self.button1.destroy()
        self.button1 = Button(self, text="undisplay",
                              command=self.undisplay)
        self.button1.grid(row=0, column=0, padx=50)
        self.update_fig()

    def undisplay(self):
        global xs, ys
        self.display_chart = False
        self.canvas.get_tk_widget().destroy()
        xs = []
        ys = []
        ax.clear()
        # ax.plot(xs, ys)
        # self.canvas.draw()

        self.button1.destroy()
        self.button1 = Button(self, text="Display",
              command=self.display)
        self.button1.grid(row=0, column=0, padx=50)




root = Root()
root.mainloop()

