import engine

world = engine.TerrainEngine(
    height = 200,
    width = 200,

    periodX= 4,
    periodY = 4,

    seed = 0,
    dimension = "3D",
    water_level= 0
    )
world.generate()
""" 
Make visual area shorter proportionally to water level 
Make a seed generator (Way to save numpy.random.seed every new gen for export later).
Make way to re-create maps
GUI
"""