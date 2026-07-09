import numpy as np


# Problem 1
def calculate_buoyancy(self):
    g = 9.81
    fluid_density = 1000
    volume = self.volume
    buoyant_force = fluid_density * volume * g
    return buoyant_force

# Problem 2
def will_it_float(self):
    buoyant_force = self.calculate_buoyancy()
    V = self.volume
    mass = self.mass
    weight = mass * 9.81
    if buoyant_force > weight:
        return True
    else:
        if buoyant_force == weight:
            return "The object is neutrally buoyant"
        else:
            return False

# Problem 3
def calculate_pressure(self):
    g = 9.81
    fluid_density = 1000
    depth = self.depth
    pressure = fluid_density * g * depth
    return pressure

    