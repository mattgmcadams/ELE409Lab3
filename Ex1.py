from tkinter import *
from sense_hat import SenseHat
sense = SenseHat()

class getSense(object):
    def getTemp(self): return round(sense.get_temperature(), 2)

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Temperature")
        self.geometry("200x180")
        self.sensing = getSense()
        self.topic = Label(self, text="Temperature Monitor")
        self.topic.grid(row=0,column=0,columnspan=2,pady=10)
        self.label = Label(self, text="Temperature is:")
        self.label.grid(row=1,column=0,pady=10)
        self.text = Text(self, height = 1, width = 10)
        self.text.grid(row=1,column=1, pady=10)
        temp = str(self.sensing.getTemp()) + " C"
        self.text.insert(END, temp)

    def update_temp(self):
        temp = str(self.sensing.getTemp()) + " C"
        self.text.delete("1.0", END)
        self.text.insert(END, temp)
        self.after(1000,self.update_temp)


root = Root()

root.mainloop()