from Repository import FakeRepository


class IngredientRepository(FakeRepository.FakeRepository):
    def __init__(self):
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def remove(self, ingredient):
        if self.ingredients:
            for p in self.ingredients:
                if p.name == ingredient.name:
                    self.ingredients.remove(p)

    def get_all(self):
        return self.ingredients

    def get_by_name(self, name):
        if self.ingredients:
            for p in self.ingredients:
                if p.name == name:
                    return p
        return "Ингредиент не найден"