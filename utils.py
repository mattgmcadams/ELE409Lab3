from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.clear()

R = (255,0,0)
y_coord = 3
x_coord = 3

sense.set_pixel(x_coord, y_coord, R)

def update():
    global x_coord, y_coord
    sense.set_pixel(x_coord, y_coord, R)
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                if y_coord > 0:
                    sense.clear()
                    y_coord = y_coord - 1
                    sense.set_pixel(x_coord,y_coord,R)
                else:
                    sleep(1)
                    sense.clear()
                    x_coord = 3
                    y_coord = 3
                    sense.set_pixel(x_coord, y_coord, R)
            elif event.direction == "down":
                if y_coord < 7:
                    sense.clear()
                    y_coord = y_coord + 1
                    sense.set_pixel(x_coord, y_coord, R)
                else:
                    sleep(1)
                    sense.clear()
                    x_coord = 3
                    y_coord = 3
                    sense.set_pixel(x_coord, y_coord, R)
            elif event.direction == "left":
                if x_coord > 0:
                    sense.clear()
                    x_coord = x_coord - 1
                    sense.set_pixel(x_coord, y_coord, R)
                else:
                    sleep(1)
                    sense.clear()
                    x_coord = 3
                    y_coord = 3
                    sense.set_pixel(x_coord, y_coord, R)
            elif event.direction == "right":
                if x_coord < 7:
                    sense.clear()
                    x_coord = x_coord + 1
                    sense.set_pixel(x_coord, y_coord, R)
                else:
                    sleep(1)
                    sense.clear()
                    x_coord = 3
                    y_coord = 3
                    sense.set_pixel(x_coord, y_coord, R)
