from Calories import Calories

from Diary import Diary
from Diet import Diet
from Dish import Dish
from FakeRepository import FakeRepository
from Ingredient import Ingredient
from Macronutrients import Macronutrients
from Person import Person


def main():
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
    print(f"Person Name: {retrieved_person.name}")
    print(f"Diary ID: {retrieved_person.diary.diary_id}")
    print(f"Diet Name: {retrieved_person.diet.name}")
    print(f"Dish Name in Diary: {retrieved_person.diary.dishes[0].name}")
    print(f"Ingredients in Dish: {[ingredient.name for ingredient in retrieved_person.diary.dishes[0].ingredients]}")
    print(f"Macronutrients: Protein {retrieved_person.diary.dishes[0].macronutrients.protein}, "
          f"Fat {retrieved_person.diary.dishes[0].macronutrients.fat}, "
          f"Carbs {retrieved_person.diary.dishes[0].macronutrients.carbs}")
    print(f"Calories: {retrieved_person.diary.dishes[0].calories.amount}")

if __name__ == "__main__":
    main()
