class Dish:
    def __init__(self, dish_id, name, macronutrients, calories):
        self.dish_id = dish_id
        self.name = name
        self.macronutrients = macronutrients
        self.calories = calories
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)