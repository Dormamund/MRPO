class Dish:
    def __init__(self, dish_id, name, macronutrients, calories):
        self.dish_id = dish_id
        self.name = name
        self.macronutrients = macronutrients
        self.calories = calories
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __eq__(self, other):
        if isinstance(other, Dish):
            return (self.dish_id == other.dish_id and self.name == other.name and
                    self.macronutrients == other.macronutrients and self.calories == other.calories)
        return False