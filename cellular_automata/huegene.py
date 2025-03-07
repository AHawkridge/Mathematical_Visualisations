
import matplotlib.pyplot as plt
import numpy as np

def generate_colors_from_cmap(n, cmap_name='hsv'):
    cmap = plt.get_cmap(cmap_name)
    colors = [cmap(i/n) for i in range(n)]
    return colors

# Generate 10 colors from the hsv colormap
colors_cmap = generate_colors_from_cmap(10)

# Example plot: drawing horizontal lines with each color from the colormap
for i, color in enumerate(colors_cmap):
    plt.plot([0, 1], [i, i], color=color, linewidth=5)

plt.title("Hue Generator from hsv colormap")
plt.xlabel("X-axis")
plt.ylabel("Line Index")
plt.show()
