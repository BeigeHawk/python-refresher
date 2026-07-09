import numpy as np


# Problem 1
def calculate_buoyancy(self):
    g = 9.81
    fluid_density = 1000
    volume = self.volume
    buoyant_force = fluid_density * volume * g
    return buoyant_force