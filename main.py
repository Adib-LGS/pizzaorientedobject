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


class MyPizza(Pizza):

    def __init__(self):
        super().__init__("Eddit", 0, [])
        self.ask_user_ingredients()

    def ask_user_ingredients(self):
        while True:
            ingredients = input("Add some ingredients (or press Enter to exit) : ")
            if ingredients == "":
                return  # exit from method
            self.ingredients.append(ingredients)
            print(f"You've added {len(self.ingredients)} ingredients : {self.ingredients}")


pizzas = [
    Pizza("4 seasons", 10.50, ("mozza", "mushrooms", "spinach", "olive oil"), True),
    Pizza("liberta", 11.50, ("tuna", "eggs", "onions", "tomatoes")),
    Pizza("samoan", 09.50, ("chiken", "potatoes", "mustard", "salad")),
    MyPizza()
]


def sort_pizzas(e):
    return len(e.name)


# pizzas.sort(key=sort_pizzas, reverse=True)


for i in pizzas:
    i.show()
