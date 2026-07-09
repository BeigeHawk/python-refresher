import numpy as np


# Problem 1
def calculate_buoyancy(self):
    g = 9.81
    volume = self.volume # Cubic meters
    density_fluid = self.density_fluid # Kilograms per cubic meter
    buoyant_force = density_fluid * volume * g
    return buoyant_force # Newtons

# Problem 2
def will_it_float(self):
    buoyant_force = self.calculate_buoyancy()
    V = self.volume # Cubic meters
    mass = self.mass # Kilograms
    weight = mass * 9.81 # Meters per second squared
    if buoyant_force > weight:
        return True
    else:
        if buoyant_force == weight:
            return "The object is neutrally buoyant"
        else:
            return False

# Problem 3
def calculate_pressure(self):
    g = 9.81 # Meters per second squared
    density_fluid = self.density_fluid # Kilograms per cubic meter
    depth = self.depth # Meters
    pressure = density_fluid * g * depth
    return pressure # Pascals

# Problem 4
def calculate_acceleration(self):
    F = self.force # Newtons
    m = self.mass # Kilograms
    acceleration = F / m
    return acceleration # Meters per second squared

# Problem 5
def calculate_angular_acceleration(self):
    tau = self.torque # Newton-meters
    I = self.moment_of_inertia # kg * m^2
    angular_acceleration = tau / I
    return angular_acceleration

# Problem 6
def calculate_torque(self):
    F_magnitude = self.force_magnitude # Newtons
    F_direction = self.force_direction # Degrees
    r = self.position_vector # Meters
    torque = np.cross(r, F_magnitude * F_direction)
    return torque

# Problem 7
def calculate_moment_of_inertia(self):
    m = self.mass # Kilograms
    r = self.radius # Meters
    moment_of_inertia = 0.5 * m * r ** 2
    return moment_of_inertia

# Problem 8
def calculate_auv_acceleration(self):
    F_magnitude = self.force_magnitude # Newtons
    F_angle = self.force_angle # Radians
    mass = self.mass # Kilograms, default is 100 kg
    volume = self.volume # Cubic meters, default is 0.1 m^3
    thruster_distance = self.thruster_distance # Meters
