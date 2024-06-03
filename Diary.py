class Diary:
    def __init__(self, diary_id, person):
        self.diary_id = diary_id
        self.person = person
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def __eq__(self, other):
        if isinstance(other, Diary):
            return self.diary_id == other.diary_id and self.person == other.person
        return False
