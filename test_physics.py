import unittest
import physics
import numpy as np


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(volume = 0.5, density_fluid = 1000), 4905.0)
        self.assertEqual(physics.calculate_buoyancy(volume = 1, density_fluid = 1000), 9810.0)
        self.assertEqual(physics.calculate_buoyancy(volume = 2, density_fluid = 1000), 19620.0)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(volume = 0.5, density_fluid = 1000, mass = 400), True)
        self.assertEqual(physics.will_it_float(volume = 0.5, density_fluid = 1000, mass = 500), "The object is neutrally buoyant")
        self.assertEqual(physics.will_it_float(volume = 0.5, density_fluid = 1000, mass = 600), False)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(density_fluid = 1000, depth = 10), 98100.0)
        self.assertEqual(physics.calculate_pressure(density_fluid = 1000, depth = 20), 196200.0)
        self.assertEqual(physics.calculate_pressure(density_fluid = 1000, depth = 30), 294300.0)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(force = 10, mass = 2), 5.0)
        self.assertEqual(physics.calculate_acceleration(force = 20, mass = 4), 5.0)
        self.assertEqual(physics.calculate_acceleration(force = 20, mass = 8), 2.5)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(tau = 10, I = 2), 5.0)
        self.assertEqual(physics.calculate_angular_acceleration(tau = 20, I = 4), 5.0)
        self.assertEqual(physics.calculate_angular_acceleration(tau = 20, I = 8), 2.5)

    def test_calculate_torque(self):
        self.assertEqual(physics.calculate_torque(F_magnitude = 10, F_direction = np.array([1, 0, 0]), r = np.array([0, 1, 0])), np.array([0, 0, -10]))

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(m = 2, r = 3), 9.0)
        self.assertEqual(physics.calculate_moment_of_inertia(m = 4, r = 2), 8.0)
        self.assertEqual(physics.calculate_moment_of_inertia(m = 6, r = 1), 3.0)