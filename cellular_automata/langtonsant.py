import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import itertools

background = "#2e261f"
foreground = "#ebdac6"
yellow = "#da9a1b"
red = "#f35044"
blue = "#46a9b4"

custom_cmap = ListedColormap([background, yellow, red, blue])
N = 50

fig, ax = plt.subplots()
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
fig.set_size_inches(5, 5) 
# ant [x,y,rotation,team]
ants = [[25,5,0,2],[25,15,0,3],[25,25,0,1],[25,35,0,2],[25,45,0,3]]

ax.axis('off')
grid = np.zeros([N, N]).reshape(N, N)


for ant in ants:
    row, col, direction, team = ant
    grid[row, col] = team

img = ax.imshow(grid, cmap=custom_cmap, interpolation="none")


def update(frame):
    global grid
    new_grid = grid.copy()

    for ant in ants:
        i, j, direction, team = ant

        if grid[i % N, j % N] != team:
            new_grid[i % N, j % N] = team
            direction = (direction + 1) % 4
        else:
            new_grid[i % N, j % N] = 0
            direction = (direction - 1) % 4

        if direction == 0:
            ant[0] = (ant[0] + 1) % N
        elif direction == 1:
            ant[1] = (ant[1] + 1) % N
        elif direction == 2:
            ant[0] = (ant[0] - 1) % N
        elif direction == 3:
            ant[1] = (ant[1] - 1) % N

        ant[2] = direction

    grid = new_grid.copy()
    img.set_data(new_grid)
    return (img,)


an = animation.FuncAnimation(
    fig, update, frames=3000, interval=0, cache_frame_data=False, blit=True
)

an.save("anims/ants.gif", writer="pillow", fps=60)
plt.show()
