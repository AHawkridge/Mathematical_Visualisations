import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import itertools

fig, ax = plt.subplots()
ax.axis("off")
ax.set_aspect("equal")

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

(line,) = ax.plot([], [], color="rebeccapurple")
n = 2
d = 1
k = n / d

xs = []
ys = []
theta = 0


def init():
    line.set_data([], [])
    return line


def update(frame):
    global theta, n, d, xs, ys
    theta += np.pi / 100 
    T = 2 * np.pi*d +1
    if n ==d:
        T = np.pi +1
    if theta >= T:
        theta = 0
        xs = []
        ys = []
        if n < 7:
            n += 1
        elif d < 9:
            n = 1
            d += 1
        else:
            n = 1
            d = 1
    k = n / d
    r = np.cos(k * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    xs.append(x)
    ys.append(y)

    line.set_data(xs, ys)
    return (line,)


ani = animation.FuncAnimation(
    fig,
    update,
    frames=1000,
    init_func=init,
    interval=5,
)

fig.set_size_inches(5, 5)
ani.save("anims/rose.gif", writer="pillow", fps=30)
plt.show()
