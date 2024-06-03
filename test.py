import unittest
from Calories import Calories
from Diary import Diary
from Diet import Diet
from Dish import Dish
from FakeRepository import FakeRepository
from Ingredient import Ingredient
from Macronutrients import Macronutrients
from Person import Person
from business_rules import assign_diary_to_person, assign_diet_to_person, add_dish_to_diet, add_ingredient_to_dish, \
    add_dish_to_diary


class TestBusinessRules(unittest.TestCase):
    def setUp(self):
        self.repo = FakeRepository()
        self.person = Person(1, "John Doe")
        self.diary = Diary(1, self.person)
        self.diet = Diet(1, "Keto")
        self.macronutrients = Macronutrients(20, 30, 50)
        self.calories = Calories(500)
        self.dish = Dish(1, "Salad", self.macronutrients, self.calories)
        self.ingredient1 = Ingredient(1, "Lettuce")
        self.ingredient2 = Ingredient(2, "Tomato")

    def test_assign_diary_to_person(self):
        assign_diary_to_person(self.person, self.diary)
        self.assertEqual(self.person.diary, self.diary)

    def test_assign_diet_to_person(self):
        assign_diet_to_person(self.person, self.diet)
        self.assertEqual(self.person.diet, self.diet)

    def test_add_dish_to_diet(self):
        add_dish_to_diet(self.diet, self.dish)
        self.assertIn(self.dish, self.diet.dishes)

    def test_add_ingredient_to_dish(self):
        add_ingredient_to_dish(self.dish, self.ingredient1)
        self.assertIn(self.ingredient1, self.dish.ingredients)

    def test_add_dish_to_diary(self):
        add_dish_to_diary(self.diary, self.dish)
        self.assertIn(self.dish, self.diary.dishes)

    def test_person_can_have_only_one_diary(self):
        diary2 = Diary(2, self.person)
        assign_diary_to_person(self.person, self.diary)
        with self.assertRaises(ValueError):
            assign_diary_to_person(self.person, diary2)

    def test_person_can_have_only_one_diet(self):
        diet2 = Diet(2, "Vegan")
        assign_diet_to_person(self.person, self.diet)
        with self.assertRaises(ValueError):
            assign_diet_to_person(self.person, diet2)

if __name__ == "__main__":
    unittest.main()