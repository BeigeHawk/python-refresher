import numpy as np


# Problem 1
def calculate_buoyancy(volume, density_fluid):
    g = 9.81
    buoyancy = volume * density_fluid * g
    return buoyancy

# Problem 2
def will_it_float(volume, density_fluid, mass):
    g = 9.81
    buoyant_force = volume * density_fluid * g
    weight = mass * g
    if buoyant_force > weight:
        return True
    else:
        if buoyant_force == weight:
            return "The object is neutrally buoyant"
        else:
            return False

# Problem 3
def calculate_pressure(density_fluid, depth):
    g = 9.81
    pressure = density_fluid * g * depth
    return pressure

# Problem 4
def calculate_acceleration(force, mass):
    acceleration = force / mass
    return acceleration

# Problem 5
def calculate_angular_acceleration(tau, I):
    angular_acceleration = tau / I
    return angular_acceleration

# Problem 6
def calculate_torque(F_magnitude, F_direction, r):
    torque = np.cross(r, F_magnitude * F_direction)
    return torque

# Problem 7
def calculate_moment_of_inertia(m, r):
    moment_of_inertia = 0.5 * m * r ** 2
    return moment_of_inertia
"""
# Problem 8
def calculate_auv_acceleration(F_magnitude, F_angle, mass, volume, thruster_distance):
"""