class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name
        self.diary = None
        self.diet = None

    def set_diary(self, diary):
        self.diary = diary

    def choose_diet(self, diet):
        self.diet = diet

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.person_id == other.person_id and self.name == other.name
        return False