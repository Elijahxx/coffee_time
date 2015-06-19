import unittest
from coffeelite.ledger import *

class TestCustomer(unittest.TestCase):
    def test___init__(self):
        customer = Customer(name='Tom', balance=1550)
        self.test_type_of_attributes(customer)
        self.assertEqual(customer.name, 'Tom')
        self.assertEqual(customer.balance, 1550)

    def test_type_of_attributes(self,customer=Customer()):
        self.assertEqual(type(customer.name), type(str()))
        self.assertEqual(type(customer.balance), type(int()))

    def test___repr__(self):
        customer = Customer(name='Jing', balance=1650)
        self.assertEqual("Jing. Balance = 1650", customer.__repr__())

    def test_credit(self):
        customer = Customer(balance=1500)
        customer.credit(150)
        self.assertEqual(1650, customer.balance)

    def test_debit(self):
        customer = Customer(balance=1500)
        customer.debit(150)
        self.assertEqual(1350, customer.balance)
        customer.debit(1350)
        self.assertEqual(0, customer.balance)

    def test_doesnt_debit_when_no_balance(self):
        customer = Customer(balance=0)
        try:
            customer.debit(100)
        except:
            pass
        self.assertEqual(0, customer.balance)

    def test_doesnt_debit_when_not_enough(self):
        customer = Customer(balance=900)
        try:
            customer.debit(1000)
        except:
            pass
        self.assertEqual(900, customer.balance)



class TestLedger(unittest.TestCase):
    def test___init__(self):
        ledger = Ledger()
        self.assertIsInstance(ledger,Ledger)
        self.assertEqual([],ledger.customers)

if __name__ == '__main__':
    unittest.main()
