from tkinter import *
from sense_hat import SenseHat
sense = SenseHat()


class getSense(object):
    def getTemp(self):  return sense.get_temperature()
    def getHum(self):   return round(sense.get_humidity(), 2)
    def getPress(self): return round(sense.get_pressure(), 2)


class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.temp_units = 'C'
        self.humidity_unit = '%'
        self.pressure_unit = ' hPa'
        self.title("Temperature")
        self.geometry("300x200")
        self.sensing = getSense()
        self.topic = Label(self, text="Temp Pressure and Humidity Monitor")
        self.topic.grid(row=0, column=0, columnspan=2, pady=10)
        # display temperature
        self.temp_label = Label(self, text="Temperature:")
        self.temp_label.grid(row=1,column=0,pady=10)
        self.temp_text = Text(self, height=1, width=10)
        self.temp_text.grid(row=1, column=1, pady=10)
        self.temp = str(self.sensing.getTemp()*(9/5)+32) + self.temp_units[0]
        self.temp_text.insert(END, self.temp)
        # display pressure
        self.pressure_label = Label(self, text="Pressure: ")
        self.pressure_label.grid(row=2, column=0, pady=10)
        self.pressure_text = Text(self, height=1, width=10)
        self.pressure_text.grid(row=2, column=1, pady=10)
        pressure = str(self.sensing.getPress()) + self.pressure_unit
        self.pressure_text.insert(END, pressure)
        # display humidity
        self.humidity_label = Label(self, text="Humidity: ")
        self.humidity_label.grid(row=3, column=0, pady=10)
        self.humidity_text = Text(self, height=1, width=10)
        self.humidity_text.grid(row=3, column=1, pady=10)
        humidity = str(self.sensing.getHum()) + self.humidity_unit
        self.humidity_text.insert(END, humidity)
        self.temp_button = Button(self, text="Convert temp",
                              command=self.convert_temp)
        self.update_temp()
        self.update_pressure()
        self.update_humidity()

    def update_temp(self):
        if self.temp_units == 'C':
            self.temp = str(round(self.sensing.getTemp(), 2)) + " C"
        else:
            self.temp = str(round(self.sensing.getTemp()*(9/5)+32, 2)) + " F"
        self.temp_text.delete("1.0", END)
        self.temp_text.insert(END, self.temp)
        self.after(5000, self.update_temp)

    def update_pressure(self):
        pressure = str(self.sensing.getPress()) + self.pressure_unit
        self.pressure_text.delete("1.0", END)
        self.pressure_text.insert(END, pressure)
        self.after(5000, self.update_pressure)

    def update_humidity(self):
        humidity = str(self.sensing.getHum()) + self.humidity_unit
        self.humidity_text.delete("1.0", END)
        self.humidity_text.insert(END, humidity)
        self.after(5000, self.update_humidity)

    def convert_temp(self):
        self.temp_units = 'F'
        self.temp = str(round(self.sensing.getTemp()*(9/5)+32, 2)) + " F"
        self.temp_text.delete("1.0", END)
        self.temp_text.insert(END, self.temp)
        self.after(5000, self.update_temp)

root = Root()

root.mainloop()
