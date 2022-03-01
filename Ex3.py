from tkinter import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
import numpy as np

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# This function is called periodically from FUncAnimation
def animate(i):
    global xs, ys
    data = np.random.normal()
    time = dt.datetime.now().strftime('%H:%M:%S')
    # add y and x to lists
    xs.append(time)
    ys.append(data)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    #format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=.30)
    plt.title('Gaussian Variables')
    plt.ylabel('Gaussian Value')
    plt.pause(1)
    
# Set up the plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate)
plt.show()