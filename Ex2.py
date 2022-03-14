from tkinter import *
from sense_hat import SenseHat
sense = SenseHat()


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Get Inputs")
        self.geometry("360x200")
        self.topic = Label(self, text="Display text on Sense Hat")
        self.topic.grid(row=0, column=0, columnspan=3, pady=20)
        self.label = Label(self, text="Text to display:")
        self.label.grid(row=1, column=0, pady=20, padx=10)
        self.entry = Entry(self, width=15)
        self.entry.grid(row=1, column=1, pady=20)
        self.button1 = Button(self, text="Display",
                              command=self.display)
        self.button1.grid(row=1, column=2, pady=20, padx=10)
        self.input = None

    def display(self):
        self.input = self.entry.get()
        sense.show_message(self.input)

root = Root()
root.mainloop()
