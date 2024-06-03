from Calories import Calories
from Diary import Diary
from Diet import Diet
from Dish import Dish
from FakeRepository import FakeRepository
from Ingredient import Ingredient
from Macronutrients import Macronutrients
from Person import Person


def assign_diary_to_person(person, diary):
    if person.diary is not None:
        raise ValueError("Person already has a diary.")
    person.set_diary(diary)

def assign_diet_to_person(person, diet):
    if person.diet is not None:
        raise ValueError("Person already has a diet.")
    person.choose_diet(diet)

def add_dish_to_diet(diet, dish):
    diet.add_dish(dish)

def add_ingredient_to_dish(dish, ingredient):
    if ingredient not in dish.ingredients:
        dish.add_ingredient(ingredient)

def add_dish_to_diary(diary, dish):
    if dish not in diary.dishes:
        diary.add_dish(dish)

# Example usage of business rules:
repo = FakeRepository()

# Создание экземпляров
person = Person(1, "John Doe")
diary = Diary(1, person)
diet = Diet(1, "Keto")
macronutrients = Macronutrients(20, 30, 50)
calories = Calories(500)
dish = Dish(1, "Salad", macronutrients, calories)
ingredient1 = Ingredient(1, "Lettuce")
ingredient2 = Ingredient(2, "Tomato")

# Применение бизнес правил
try:
    assign_diary_to_person(person, diary)
    assign_diet_to_person(person, diet)
    add_dish_to_diet(diet, dish)
    add_ingredient_to_dish(dish, ingredient1)
    add_ingredient_to_dish(dish, ingredient2)
    add_dish_to_diary(diary, dish)
except ValueError as e:
    print(e)

# Добавление экземпляров в репозиторий
repo.add_person(person)
repo.add_diary(diary)
repo.add_diet(diet)
repo.add_dish(dish)
repo.add_ingredient(ingredient1)
repo.add_ingredient(ingredient2)

# Извлекаем и используем экземпляры
retrieved_person = repo.get_person(1)
print(f"Person Name: {retrieved_person.name}")
print(f"Diary ID: {retrieved_person.diary.diary_id}")
print(f"Diet Name: {retrieved_person.diet.name}")
print(f"Dish Name in Diary: {retrieved_person.diary.dishes[0].name}")
print(f"Ingredients in Dish: {[ingredient.name for ingredient in retrieved_person.diary.dishes[0].ingredients]}")
print(f"Macronutrients: Protein {retrieved_person.diary.dishes[0].macronutrients.protein}, "
      f"Fat {retrieved_person.diary.dishes[0].macronutrients.fat}, "
      f"Carbs {retrieved_person.diary.dishes[0].macronutrients.carbs}")
print(f"Calories: {retrieved_person.diary.dishes[0].calories.amount}")