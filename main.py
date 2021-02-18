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
    BASE_PRICE = 8
    INGREDIENT_PRICE: float = 1.50
    last_order_number = 0

    def __init__(self):
        MyPizza.last_order_number += 1  # All the class
        self.myorder_number = MyPizza.last_order_number
        super().__init__("Eddit " + str(self.myorder_number), 0, [])
        self.ask_user_ingredients()
        self.amount()

    def ask_user_ingredients(self):
        print()
        print(f"Ingredients for the eddited pizza {self.myorder_number}")
        while True:
            ingredients = input("Add some ingredients (or press Enter to exit) : ")
            if ingredients == "":
                return  # exit from method
            self.ingredients.append(ingredients)
            print(f"You've added {len(self.ingredients)} ingredients : {self.ingredients}")

    def amount(self):
        if len(self.ingredients) > 0:
            self.price = self.BASE_PRICE + len(self.ingredients)*self.INGREDIENT_PRICE
        else:
            self.price = self.BASE_PRICE


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
