from dataclasses import dataclass
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


    seed: int
    dimension: str #2D or 3D

    octaves: Optional[int] = 1
    water_level: Optional[float] = None

    def generate(self):

        numpy.random.seed(self.seed)
       
        # Generate noise terrain:
        noise = generate_fractal_noise_2d((self.height, self.width), (self.periodX, self.periodY))
        
        # Set Water Level 
        if self.water_level is not None:
            noise[noise <= self.water_level]= self.water_level 

        # Output 2D Terrain
        if self.dimension == "2D":
            terrain_plot = plt.imshow(noise, cmap='terrain')

        # Output 3D Terrain
        elif self.dimension == "3D":
            # Make three dimensional visualization using concentration as height
            x_coords, y_coords = numpy.meshgrid(numpy.arange(self.height), numpy.arange(self.width))
            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            terrain_plot = ax.plot_surface(x_coords, y_coords, noise, cmap='terrain', linewidth = 0)

        else:
            raise NameError
        plt.show()        
