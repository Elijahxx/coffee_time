class Tube(object):
    def __init__(self, coffee_type='espresso', quantity=0):
        self.coffee_type = coffee_type
        self.quantity = quantity

class Vendor(object):
    def __init__(self, *args):
        self.coffee_types = []
        for coffee_type in args:
            self.coffee_types.append(coffee_type)


if __name__ == "__main__":
    vendor = Vendor('espresso','intenso','lungo','decaffeinato','caramelito')

    # Tom wants to buy some coffee. He browses the choices
    print vendor.coffee_types


