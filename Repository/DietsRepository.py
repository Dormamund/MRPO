from Repository import FakeRepository


class DietsRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.diets = []

    def add(self, diet):
        self.diets.append(diet)

    def remove(self, diet):
        if self.diets:
            for c in self.diets:
                if c.name == diet.name:
                    self.diets.remove(c)

    def get_all(self):
        return self.diets

    def get_by_name(self, name):
        if self.diets:
            for c in self.diets:
                if c.name == name:
                    return c
        return "Категория не найдена"