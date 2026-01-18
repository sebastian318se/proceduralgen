import matplotlib.pyplot as plt
import tkinter
import numpy
from perlin_numpy import (generate_fractal_noise_2d, generate_perlin_noise_2d)

# Set UI root
# root = tkinter.Tk()
# root.geometry("750x750")
# root.title("Mini-Map Procedural Gen")

# root.configure(bg = "gainsboro")

noise = generate_perlin_noise_2d((60, 60), (5, 5)) # Lower second tuple for smoother table
plt.imshow(noise, cmap='gray', interpolation='lanczos')
plt.colorbar()
plt.show()
"""
Get Smooth Perlin Noise (Adjusting Frequency)
Convert to scale 0 - 1.0
Grid
Output Image. Process into matplotlib, proper colors and scalability
Display in GUI

Simple menu for adjusting size or re-generating the current map
"""

# root.mainloop()