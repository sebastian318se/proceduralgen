from dataclasses import dataclass, field
from typing import Optional
import matplotlib.pyplot as plt
import numpy
from perlin_numpy import generate_perlin_noise_2d, generate_fractal_noise_2d

@dataclass
class TerrainEngine:
    height: int # Terrain dimension
    width: int

    periodX: int # Rougher or smoother terrain 
    periodY: int

    dimension: str #2D or 3D

    seed: Optional[int] = None
    octaves: Optional[int] = 1
    water_level: Optional[float] = None

    def generate(self):

        global x_coords, y_coords, noise
        numpy.random.seed(self.seed)
       
        # Generate noise terrain:
        noise = generate_fractal_noise_2d((self.height, self.width), (self.periodX, self.periodY))
        
        # Set Water Level 
        if self.water_level is not None:
            noise[noise <= self.water_level]= self.water_level 

        # Output 2D Terrain
        if self.dimension == "2D":
            return noise
            
        # Output 3D Terrain
        elif self.dimension == "3D":
            # Make three dimensional visualization using concentration as height
            x_coords, y_coords = numpy.meshgrid(numpy.arange(self.height), numpy.arange(self.width))

        else:
            raise NameError
    
    # Axes passed as arguments so it works both as standalone and w/ ui appl.
    def draw(self, ax, fig):
        global x_coords, y_coords, noise
        if self.dimension == "2D":
            ax.imshow(noise, cmap='terrain')
        else:
            ax.plot_surface(x_coords, y_coords, noise, cmap = 'terrain', linewidth = 0)
""""
TODO

Make visual area shorter proportional to water level -> adjust plt axis-ratio
Make vertical walls not water whenever water level is active
Make a seed generator (Way to save numpy.random.seed every new gen for export later).
Make way to re-create maps
GUI
"""