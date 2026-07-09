import numpy as np


# Problem 1
def calculate_buoyancy(self):
    g = 9.81
    fluid_density = 1000
    volume = self.volume
    buoyant_force = fluid_density * volume * g
    return buoyant_force

# Problem 2
def calculate_pressure(self):
    g = 9.81
    fluid_density = 1000
    depth = self.depth
    pressure = fluid_density * g * depth
    return pressure

