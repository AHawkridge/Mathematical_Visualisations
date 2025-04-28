import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import itertools

fig, ax = plt.subplots()
# Set custom colours.
background = "#2e261f"
foreground = "#ebdac6"
yellow = "#da9a1b"
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
fig.set_size_inches(5, 5) 
ax.set_aspect("equal")
custom_cmap = ListedColormap(['white', 'black'])
N = 1
0

grid = np.zeros([N, N]).reshape(N, N)

grid[50,50] = 1
grid[51,50] = 1
grid[51,51] = 1
grid[51,49] = 1

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
text = ax.text(5, 5, "", color=yellow, fontsize=14)
img = ax.imshow(grid, cmap=custom_cmap, interpolation="none")

def update(frameNum):
    global grid
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = (
                grid[(i - 1) % N, (j - 1) % N]
                + grid[(i - 1) % N, j]
                + grid[(i - 1) % N, (j + 1) % N]
                + grid[i, (j - 1) % N]
                + grid[i, (j + 1) % N]
                + grid[(i + 1) % N, (j - 1) % N]
                + grid[(i + 1) % N, j]
                + grid[(i + 1) % N, (j + 1) % N]
            )

            if total == 2: 
                newGrid[i, j] = 1
            else:
                newGrid[i,j]= 0

    grid = newGrid.copy()
    img.set_data(grid)
    return img, text

an = animation.FuncAnimation(
    fig,
    update,
    frames=itertools.count(),
    interval=30,
    cache_frame_data=False,
    blit=True,
)
ax.axis('off')
# an.save("anims/game_of_life.gif", writer="pillow", fps=30)
plt.show()
