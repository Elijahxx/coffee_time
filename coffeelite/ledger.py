class Customer(object):
    def __init__(self, name='ghost', balance=0.0):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return "%s. Balance = %.2f" % (self.name, self.balance)

    def debit(self, amount):
        print "Debiting %.2f from %s" % (amount, self.name)
        self.balance -= amount
        print "%s now has %.2f" % (self.name, self.balance)

    def credit(self, amount):
        print "Crediting %.2f to %s" % (amount, self.name)
        self.balance += amount
        print "%s now has %.2f" % (self.name, self.balance)


class Ledger(object):
    def __init__(self):
        self.customers = []


if __name__ == "__main__":
    ledger = Ledger()

