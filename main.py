class Pizza:

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def show(self):
        print(f"PIZZA: {self.name} : {self.price} $")
        print(", ".join(self.ingredients)) # Show All ingredients in Tuples properly


pizza1 = Pizza("4 seasons", 10.50, ("mozza", "mushrooms", "spinach", "olive oil"))
pizza1.show()

