import unittest
from coffeelite.coffee import *

class TestVendor(unittest.TestCase):
    def test___init__(self):
        coffee_types = ['espresso','intenso','lungo','decaffeinato','caramelito']
        vendor = Vendor('espresso','intenso','lungo','decaffeinato','caramelito')
        self.assertEqual(coffee_types, vendor.coffee_types)

if __name__ == '__main__':
    unittest.main()
