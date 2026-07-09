import unittest
import physics
import numpy as np


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(volume = 0.5, density_fluid = 1000), 4905.0)