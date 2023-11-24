class FoodItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.availability = True

    def make_unavailable(self):
        if self.availability == False:
            raise Exception("Item already unavailable")

        self.availability = False

    def make_available(self):
        if self.availability == True:
            raise Exception("Item already available")
        
        self.availability = True

    