from ledger import Customer

class Capsule(object):
    def __init__(self, coffee_type):
        self.coffee_type = coffee_type


class Tube(object):
    def __init__(self, coffee_type='espresso', quantity=0, cost=35):
        self.coffee_type = coffee_type
        self.quantity = quantity
        self.cost = cost

    def __repr__(self):
        return "(%s, %s, %d)" % (self.coffee_type, self.quantity, self.cost)

    def dispense(self, quantity=1):
        if self.quantity < quantity:
            raise ValueError("Tried to dispense %d capsules but only %d left" % (quantity, self.quantity))
        else:
            print "Dispensing %d capsules of %s" % (quantity, self.coffee_type)
            self.quantity -= quantity
            print "%d capsules left" % self.quantity
            return [Capsule(self.coffee_type)] * quantity

    def load(self, quantity=1):
        print "Loading %d capsules of %s" % (quantity, self.coffee_type)
        self.quantity += quantity
        print "%d capsules in tube" % self.quantity


class Vendor(object):
    def __init__(self, *args):
        self.tubes = []
        for coffee_type in args:
            tube = Tube(coffee_type=coffee_type, quantity=10)
            self.tubes.append(tube)

        self.coffee_types = [tube.coffee_type for tube in self.tubes]

    def select_tube(self, coffee_type='espresso'):
        for tube in self.tubes:
            if tube.coffee_type == coffee_type:
                break
        else:
            tube = None
        return tube

    def vend(self, customer=Customer(), coffee_type='espresso', quantity=1):
        tube = self.select_tube(coffee_type)
        total_cost = tube.cost * quantity

        if total_cost <= customer.balance:
            if quantity <= tube.quantity:
                customer.debit(total_cost)
                tube.dispense(quantity)
            else:
                raise ValueError("Tried to vend %d capsules but only %d left" % (quantity, tube.quantity))
        else:
            raise ValueError("Total cost of %d too much. Balance is %d" % (total_cost, customer.balance))


if __name__ == "__main__":
    vendor = Vendor('espresso','intenso','lungo','decaffeinato','caramelito')

    # A customer called Tom approaches
    tom = Customer(name='Tom', balance=1300)  # TODO: class Balance inherit from int, balance.pounds = float
    print tom

    # Tom wants to buy some coffee. He browses the choices
    print vendor.coffee_types

    # Tom wants to see how much of each coffee type there is (in each tube) and cost
    for tube in vendor.tubes:
        print tube

    # Tom checks his balance
    print tom.balance

    # Tom decides to buy two espressos and one decaffeinato
    vendor.vend(tom, 'espresso', 2)
    vendor.vend(tom, 'decaffeinato')
