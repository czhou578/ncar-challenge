'''
This is the unit testing suite for the volume calculating function
'''

import unittest
from ncar.parameterization import volume_calculate

class TestVolume(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(volume_calculate(3), 113.09733552923254)
        self.assertAlmostEqual(volume_calculate(1.5), 14.137166941154067)
        self.assertAlmostEqual(volume_calculate(0), 0)
        with self.assertRaises(ValueError):
            volume_calculate(-2)

if __name__ == '__main__':
    unittest.main()