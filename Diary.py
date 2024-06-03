class Diary:
    def __init__(self, diary_id, person):
        self.diary_id = diary_id
        self.person = person
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)