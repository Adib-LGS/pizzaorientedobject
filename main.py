class Pizza:

    def __init__(self, name, price, ingredients, veggy=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.veggy = veggy

    def show(self):
        if self.veggy:
            veg_str = " - Veggy"
            print(f"PIZZA: {self.name} : {self.price} $ " + veg_str)
        else:
            print(f"PIZZA: {self.name} : {self.price} $")
        print(", ".join(self.ingredients))  # Show All ingredients in Tuples properly
        print()


"""pizza1 = Pizza("4 seasons", 10.50, ("mozza", "mushrooms", "spinach", "olive oil"))
pizza1.show()"""

pizzas = (
    Pizza("4 seasons", 10.50, ("mozza", "mushrooms", "spinach", "olive oil"), True),
    Pizza("liberta", 11.50, ("tuna", "eggs", "onions", "tomatoes")),
    Pizza("samoan", 09.50, ("chiken", "potatoes", "mustard", "salad")),
)

for i in pizzas:
    if i.price > 10:
        i.show()
