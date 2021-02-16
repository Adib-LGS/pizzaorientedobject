class Pizza:

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def show(self):
        print(f"PIZZA: {self.name} : {self.price} $")


pizza1 = Pizza("4 seasons", 10.50)
pizza1.show()

