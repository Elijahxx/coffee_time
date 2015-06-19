import unittest
from coffeelite.coffee import *


class TestVendor(unittest.TestCase):
    def test___init__(self):
        vendor = Vendor()
        self.assertIsInstance(vendor,Vendor)


    def test_coffee_types(self):
        coffee_types = ['espresso','intenso','lungo','decaffeinato','caramelito']
        vendor = Vendor('espresso','intenso','lungo','decaffeinato','caramelito')
        self.assertEqual(coffee_types, vendor.coffee_types)


class TestTube(unittest.TestCase):
    def test___init__(self):
        coffee_type = 'espresso'
        tube = Tube('espresso')
        self.assertEqual(coffee_type, tube.coffee_type)


    def test_quantity(self):
        tube = Tube(coffee_type='espresso', quantity=5)
        self.assertEqual(5,tube.quantity)


    def test___repr__(self):
        tube = Tube('lungo', 2)
        self.assertEqual("(lungo, 2)", tube.__repr__())


    def test_type_of_attributes(self, tube=Tube()):
        self.assertEqual(type(tube.coffee_type), type(str()))
        self.assertEqual(type(tube.quantity), type(int()))

if __name__ == '__main__':
    unittest.main()
