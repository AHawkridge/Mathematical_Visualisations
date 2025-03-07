import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import itertools
from PIL import Image

iteration = 20
colormap = 'nipy_spectral'

def f(c,iterations):
    z=0
    for _ in range(iterations):
        z=z**2 + c
    return abs(z)<=2

def MandelbrotSet(c,iterations):
    z=0
    for _ in range(iterations):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
        return True

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

c = complex_matrix(-2, 0.5, -1.25, 1.25, pixel_density=512)


# image = Image.fromarray(~f(c, iterations=20))
# image.show()
# Image.effect_mandelbrot((1024, 1024), (-3, -2.5, 2, 2.5), 1000).show()


from PIL import Image
from mandelbrot_class import MandelbrotSet
from viewport import Viewport
mandelbrot_set = MandelbrotSet(max_iterations=256, escape_radius=1000)
image = Image.new(mode="L", size=(512, 512))
for pixel in Viewport(image, center=-0.7435 + 0.1314j, width=0.002):
    c = complex(pixel)
    instability = 1 - mandelbrot_set.stability(c, smooth=True)
    pixel.color = int(instability * 255)

image.show()
