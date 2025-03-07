import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patch
import itertools


# colours
red = "#F35044"
yellow = "#DA9A1B"
blue = "#46a9b4"
text = "#ebdac6"
darkbg = "#26211c"
lightbg = "#2e261f"


fig, ax = plt.subplots()
ax.set_facecolor(lightbg)
fig.patch.set_facecolor(lightbg)

(line,) = ax.plot([], [], color=red)
circle = plt.Circle((0, 0), 1, fill=True, alpha=0.4, color=text)
arc = patch.Arc((0, 0), 0.25, 0.25, theta1=0, theta2=0, color=yellow, linewidth=2)

ax.axis('off')
ax.axhline(0, color=darkbg, linewidth=1)
ax.axvline(0, color=darkbg, linewidth=1)
ax.add_patch(circle)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

ax.set_xticks([])
ax.set_yticks([])
ax.add_patch(arc)

for spine in ax.spines.values():
    spine.set_visible(False)

(h_line,) = ax.plot([], [], color=blue, linestyle="--")
(v_line,) = ax.plot([], [], color=blue, linestyle="--")
text = ax.text(-1, 1.2, "", fontsize=12, color=text)

text.set_text("")
phi = np.linspace(0, 2 * np.pi, 720)


def init():
    line.set_data([], [])
    arc.theta1 = 0
    arc.theta2 = 0
    text.set_text("")
    h_line.set_data([], [])
    v_line.set_data([], [])
    return line, arc, h_line, v_line, text


def update(frame):
    PHI = phi[frame]
    sin = np.sin(PHI)
    cos = np.cos(PHI)
    imag = [0, sin]
    real = [0, cos]

    h_line.set_data([0, cos], [sin, sin])
    v_line.set_data([cos, cos], [0, sin])

    line.set_data(real, imag)
    degrees = np.degrees(PHI)
    arc.theta2 = degrees
    text.set_text(f"φ = {degrees:.2f} \nsin(φ) = {sin:.2f} \ncos(φ) = {cos:.2f}")

    return line, arc, h_line, v_line, text


ani = FuncAnimation(fig, update, frames=len(phi), init_func=init, interval=10)
plt.show()
