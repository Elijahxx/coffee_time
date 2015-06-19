class Tube(object):
    def __init__(self, coffee_type='espresso', quantity=0):
        self.coffee_type = coffee_type
        self.quantity = quantity

    def __repr__(self):
        return "(%s, %s)" % (self.coffee_type, self.quantity)

class Vendor(object):
    def __init__(self, *args):
        self.tubes = []
        for coffee_type in args:
            tube = Tube(coffee_type=coffee_type, quantity=10)
            self.tubes.append(tube)

        self.coffee_types = [tube.coffee_type for tube in self.tubes]



if __name__ == "__main__":
    vendor = Vendor('espresso','intenso','lungo','decaffeinato','caramelito')

    # Tom wants to buy some coffee. He browses the choices
    print vendor.coffee_types

    # Tom wants to see how much of each coffee type there is (in each tube)
    for tube in vendor.tubes:
        print tube

