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
custom_cmap = ListedColormap([background, foreground])
N = 100

grid = np.random.choice([1, 0], N * N, p=[0.4, 0.6]).reshape(N, N)

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
    alive = 0
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

            if grid[i, j] == 1:
                alive += 1
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    grid = newGrid.copy()
    img.set_data(grid)
    text.set_text(f"alive = {alive}")
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
plt.show()
