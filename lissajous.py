import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import itertools

N = 1000
grid = np.zeros([N, N])

alphas = np.linspace(0, 10, N)
fig, ax = plt.subplots()

ax.axis("off")
grid = np.zeros([N, N]).reshape(N, N)

ax.set_aspect("equal")

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

(line,) = ax.plot([], [],color = 'rebeccapurple')
A = 1
B = 1
t = np.linspace(-5, 5, 1000)
delta = np.pi / 2


def init():
    line.set_data([], [])
    return line


def update(frame):
    a = alphas[frame]
    b = 1
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)

    line.set_data(y, x)
    return (line,)


ani = animation.FuncAnimation(
    fig, update, frames=len(alphas), init_func=init, interval=30
)

fig.set_size_inches(5, 5) 
ani.save("anims/lissajous.gif", writer="pillow", fps=30)
plt.show()
