class Diet:
    def __init__(self, diet_id, name):
        self.diet_id = diet_id
        self.name = name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)
