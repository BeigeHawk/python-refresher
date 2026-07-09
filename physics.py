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

# Problem 4
def calculate_acceleration(self):
    F = self.force
    m = self.mass
    acceleration = F / m
    return acceleration

# Problem 5
def calculate_angular_acceleration(self):
    tau = self.torque
    I = self.moment_of_inertia
    angular_acceleration = tau / I
    return angular_acceleration

# Problem 6
def calculate_torque(self):
    F_magnitude = self.force_magnitude
    F_direction = self.force_direction
    r = self.position_vector
    torque = np.cross(r, F_magnitude * F_direction)
    return torque

