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


    def test_select_tube(self):
        vendor = Vendor('espresso','intenso','lungo','decaffeinato','caramelito')
        tube = vendor.select_tube('intenso')
        self.assertEqual('intenso', tube.coffee_type)


    def test_vend(self):
        vendor = Vendor('espresso','intenso','lungo','decaffeinato','caramelito')
        customer = Customer(balance=1000)
        tube = vendor.select_tube('lungo') # TODO: replace tube with vendor('lungo') by setting dict as class type in Vendor
        quantity = 2

        quantity_before = tube.quantity
        balance_before = customer.balance

        vendor.vend(customer, 'lungo', quantity=quantity)

        quantity_after = tube.quantity
        balance_after = customer.balance

        cost = tube.cost*quantity

        self.assertEqual(quantity, quantity_before - quantity_after)
        self.assertEqual(cost, balance_before - balance_after)
        self.assertGreater(cost, 0)

        # TODO: assert that vendor.vend(customer, 'lungo', 2) is ('lungo', 2)
        # self.assertEqual(expected, vendor.vend(customer, coffee_type, quantity))

class TestTube(unittest.TestCase):
    def test___init__(self):
        coffee_type = 'espresso'
        tube = Tube('espresso')
        self.assertEqual(coffee_type, tube.coffee_type)


    def test_quantity(self):
        tube = Tube(quantity=5)
        self.assertEqual(5,tube.quantity)


    def test___repr__(self):
        tube = Tube(coffee_type='lungo', quantity=2, cost=30)
        self.test_type_of_attributes(tube)
        self.assertEqual("(lungo, 2, 30)", tube.__repr__())


    def test_type_of_attributes(self, tube=Tube()):
        self.assertEqual(type(tube.coffee_type), type(str()))
        self.assertEqual(type(tube.quantity), type(int()))


    def test_cost_is_strictly_positive(self):
        tube = Tube()
        self.assertGreater(tube.cost, 0)


    def capsules_test(self, capsules, quantity, coffee_type):
        self.assertEqual(quantity, len(capsules))
        for capsule in capsules:
            self.assertIsInstance(capsule, Capsule)
            self.assertEqual(capsule.coffee_type, coffee_type)


    def test_dispense(self):
        tube = Tube(coffee_type='lungo', quantity=5)

        capsules = tube.dispense(2)

        self.assertEqual(3, tube.quantity)
        self.capsules_test(capsules, quantity=2, coffee_type='lungo')

        capsules = tube.dispense()

        self.assertEqual(2, tube.quantity)
        self.capsules_test(capsules, quantity=1, coffee_type='lungo')

        capsules = tube.dispense(2)

        self.assertEqual(0, tube.quantity)
        self.capsules_test(capsules, quantity=2, coffee_type='lungo')


    def test_load(self):
        tube = Tube(coffee_type='intenso', quantity=0)

        self.assertEqual(0, tube.quantity)
        tube.load(3)
        self.assertEqual(3, tube.quantity)
        tube.load()
        self.assertEqual(4, tube.quantity)


    def test_load_and_dispense(self):
        tube = Tube(coffee_type='caramelito', quantity=0)

        tube.load()
        self.assertEqual(1, tube.quantity)
        tube.dispense()
        self.assertEqual(0, tube.quantity)
        tube.load(2)
        self.assertEqual(2, tube.quantity)
        tube.dispense(2)
        self.assertEqual(0, tube.quantity)


    def test_doesnt_dispense_when_empty(self):
        tube = Tube(quantity=0)
        try:
            tube.dispense()
        except:
            self.assertEqual(tube.quantity, 0)


    def test_doesnt_dispense_when_not_enough(self):
        tube = Tube(quantity=5)
        try:
            tube.dispense(6)
        except:
            self.assertEqual(tube.quantity, 5)


class TestCapsule(unittest.TestCase):
    def test___init__(self):
        capsule = Capsule('decaffeinato')
        self.assertIsInstance(capsule, Capsule)
        self.assertEqual('decaffeinato', capsule.coffee_type)


if __name__ == '__main__':
    unittest.main()
