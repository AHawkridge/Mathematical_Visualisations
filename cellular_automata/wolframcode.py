import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import itertools

#perosnal favourite codes.
# 99,105,62 
wolfram_code = 77 
loop = False
# wolfram_code = np.random.randint(0,255) 

code_str = np.binary_repr(wolfram_code, width=8)
code = [int(bit) for bit in code_str][::-1]

fig, ax = plt.subplots()
N = 101
background = "#2e261f"
foreground = "#ebdac6"
yellow = "#da9a1b"
red = '#f35044'
blue = '#46a9b4'
custom_cmap = ListedColormap([background, foreground])

frame_index = 1
row = np.zeros(N)
row[int(N / 2)] = 1

max_frames = int(N/2)-2  
grid = np.zeros((max_frames, N))

grid[0] = row
img = ax.imshow(grid, cmap=custom_cmap, interpolation="none", aspect="auto")


def update(frame):
    global row, grid, frame_index
    new_row = row.copy()

    for i in range(N):
        left   = row[(i - 1) % N]
        center = row[i]
        right  = row[(i + 1) % N]

        neighborhood_index = 4*left + 2*center + right
        new_row[i] = code[int(neighborhood_index)]

    row = new_row

    if frame_index < max_frames:
        grid[frame_index, :] = row
        frame_index += 1
    elif loop:
        grid = np.roll(grid, -1, axis=0)
        grid[-1, :] = row
        

    img.set_data(grid)
    return (img,)


an = animation.FuncAnimation(
    fig,
    update,
    frames=itertools.count(),
    interval=10,
    cache_frame_data=False,
    blit=True,
)

ax.axis('off')
plt.show()
