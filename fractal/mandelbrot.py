import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import itertools

fig, ax = plt.subplots()
bound = 2
max_iterations = 100 
colormap = "cubehelix" 
for i in ax.spines.values():
    i.set_visible(False) 


ax.set_aspect("equal")

func = lambda z, p, c: z**p + c
center_x, center_y = -0.75, 0.1
initial_width = 3   
initial_height = 3  

zoom_rate = 0.2  

def update(frame):
    scale = np.exp(-zoom_rate * frame)
    new_width = initial_width * scale
    new_height = initial_height * scale
    
    xstart_new = center_x - new_width / 2
    xend_new   = center_x + new_width / 2
    ystart_new = center_y - new_height / 2
    yend_new   = center_y + new_height / 2

    xDomain = np.linspace(xstart_new, xend_new, 1000)
    yDomain = np.linspace(ystart_new, yend_new, 1000)
    iterationArray = []
    for y in yDomain:
        row = []
        for x in xDomain:
            z = 0
            p = 2
            c = complex(x, y)
            for iterationNumber in range(max_iterations):
                if abs(z) >= bound:
                    row.append(iterationNumber)
                    break
                else:
                    try:
                        z = func(z, p, c)
                    except(ValueError, ZeroDivisionError):
                        z = c
            else:
                row.append(0)

        iterationArray.append(row)
    ax.clear()
    graph = ax.pcolormesh(xDomain, yDomain, iterationArray, cmap=colormap)
    return graph
ani = FuncAnimation(fig, update, frames=itertools.count(), interval=100, blit=False,cache_frame_data=False)
plt.show()

