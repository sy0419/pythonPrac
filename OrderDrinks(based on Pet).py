class OrderDrink():
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
    
    def getOrder(self):
        print("Please, select your order.")

class Bavarage(OrderDrink):
    def __init__(self, name):
        super().__init__(name, "Bavarage")

    def __str__(self):
        return f"My choice is {self.kind}/{self.name}"
    
class Alcohol(OrderDrink):
    def __init__(self, name):
        super().__init__(name, "Alcohol")

    def __str__(self):
        return f"My selection is {self.kind}/{self.name}"



order1 = Bavarage(name = "Iced tea")
order1.getOrder()
order2 = Alcohol(name = "Cass")
print(order1)
print(order2)