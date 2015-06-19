import unittest
from coffeelite.coffee import *

class TestVendor(unittest.TestCase):
    def test___init__(self):
        coffee_types = ['espresso','intenso','lungo','decaffeinato','caramelito']
        vendor = Vendor('espresso','intenso','lungo','decaffeinato','caramelito')
        self.assertEqual(coffee_types, vendor.coffee_types)


class TestTube(unittest.TestCase):
    def test__init__(self):
        coffee_type = 'espresso'
        tube = Tube('espresso')
        self.assertEqual(coffee_type, tube.coffee_type)

    def test_quantity(self):
        tube = Tube(coffee_type='espresso', quantity=5)
        self.assertEqual(5,tube.quantity)

if __name__ == '__main__':
    unittest.main()
