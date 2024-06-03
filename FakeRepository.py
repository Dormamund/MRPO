from Calories import Calories
from Diary import Diary
from Diet import Diet
from Dish import Dish
from Ingredient import Ingredient
from Macronutrients import Macronutrients
from Person import Person


class FakeRepository:
    def __init__(self):
        self.persons = {}
        self.diaries = {}
        self.diets = {}
        self.dishes = {}
        self.ingredients = {}

    def add_person(self, person):
        self.persons[person.person_id] = person

    def get_person(self, person_id):
        return self.persons.get(person_id)

    def add_diary(self, diary):
        self.diaries[diary.diary_id] = diary

    def get_diary(self, diary_id):
        return self.diaries.get(diary_id)

    def add_diet(self, diet):
        self.diets[diet.diet_id] = diet

    def get_diet(self, diet_id):
        return self.diets.get(diet_id)

    def add_dish(self, dish):
        self.dishes[dish.dish_id] = dish

    def get_dish(self, dish_id):
        return self.dishes.get(dish_id)

    def add_ingredient(self, ingredient):
        self.ingredients[ingredient.ingredient_id] = ingredient

    def get_ingredient(self, ingredient_id):
        return self.ingredients.get(ingredient_id)


# Example usage
repo = FakeRepository()

# Create instances
person = Person(1, "John Doe")
diary = Diary(1, person)
diet = Diet(1, "Keto")
macronutrients = Macronutrients(20, 30, 50)
calories = Calories(500)
dish = Dish(1, "Salad", macronutrients, calories)
ingredient1 = Ingredient(1, "Lettuce")
ingredient2 = Ingredient(2, "Tomato")

# Establish relationships
person.set_diary(diary)
person.choose_diet(diet)
diet.add_dish(dish)
dish.add_ingredient(ingredient1)
dish.add_ingredient(ingredient2)
diary.add_dish(dish)

# Add instances to the repository
repo.add_person(person)
repo.add_diary(diary)
repo.add_diet(diet)
repo.add_dish(dish)
repo.add_ingredient(ingredient1)
repo.add_ingredient(ingredient2)

# Retrieve and use instances
retrieved_person = repo.get_person(1)
print(retrieved_person.name)