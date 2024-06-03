class Dish:
    def __init__(self, id, name, cal, protein, fat, carb, ingredients, diet):
        self.id = id
        self.name = name
        self.cal = cal
        self.protein = protein
        self.fat = fat
        self.carb = carb
        self.ingredients = ingredients
        self.diet=diet

    def get_info(self):
        return [self.id, self.name, self.cal, self.protein, self.fat, self.carb, self.ingredients, self.diet]

    def __eq__(self, other):
        if isinstance(other, Dish):
            return (self.id == other.id and
                    self.name == other.name and
                    self.cal == other.cal and
                    self.protein == other.protein and
                    self.fat == other.fat and
                    self.carb == other.carb and
                    self.ingredients == other.ingredients and
                    self.diet == other.diet)
        return False