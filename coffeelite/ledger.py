class Customer(object):
    def __init__(self, name='ghost', credit=0.0):
        self.name = name
        self.credit = credit

class Ledger(object):
    def __init__(self):
        self.customers = []


if __name__ == "__main__":
    ledger = Ledger()

