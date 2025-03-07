import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N_values = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    15,
    20,
    25,
    30,
    35,
    40,
    45,
    50,
    60,
    70,
    80,
    90,
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800,
    900,
    1000,
]

fig, ax = plt.subplots()
line, = ax.plot([], [], "o-", color="#da9a1b")
# fig.set_facecolor('#da9a1b')
ax.set_facecolor("#26211c")


ax.set_xlim(-2.5, 1.1)
ax.set_ylim(-0.5, 4)
ax.set_xlabel("Real ")
ax.set_ylabel("Imaginary ")
ax.axhline(0, color="#ebdac6", linewidth=1)
ax.axvline(0, color="#ebdac6", linewidth=1)
# ax.axis('off')

text = ax.text(-2, 3, "", fontsize=12, color="#da9a1b")


def init():
    line.set_data([], [])

    text.set_text("")
    return (line, text)


def update(frame):
    N = N_values[frame]
    N = int(N)
    reals = []
    imags = []
    for m in range(N + 1):
        ez = (1 + 1j * np.pi / N) ** m
        reals.append(ez.real)
        imags.append(ez.imag)
    line.set_data(reals, imags)
    text.set_text(f"real = {ez.real:.2f}\nimag = {ez.imag:2f}")
    return (line, text)


ani = FuncAnimation(
    fig,
    update,
    frames=len(N_values),
    init_func=init,
    interval=300,
    blit=True,
    repeat=True,
)
plt.show()
