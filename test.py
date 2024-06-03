import unittest
from Dish import Dish
from business_rules import check_dish_carb, check_dish_fat, validate_nutritional_values, validate_user_height


class TestBusinessRules(unittest.TestCase):

    def setUp(self):
        self.high_carb_dish = Dish(1, "Квашеная капуста", 100, 20, 30, 1000, {}, diet='низкокалорийная')
        self.low_carb_dish = Dish(2, "Шашлык свиной", 600, 25, 15, 40, {}, diet='кето-диета')
        self.high_fat_dish = Dish(3, "Макароны по флотски", 150, 15, 25, 45, {}, diet='белковая диета')
        self.valid_dish = Dish(4, "Котлеты бабушкины", 900, 20, 20, 35, {}, diet='низкокаллорийная')

    def test_check_dish_carb(self):
        self.assertTrue(check_dish_carb(self.high_carb_dish))
        self.assertFalse(check_dish_carb(self.low_carb_dish))

    def test_check_dish_fat(self):
        self.assertTrue(check_dish_fat(self.high_fat_dish))
        self.assertFalse(check_dish_fat(self.valid_dish))

    def test_validate_nutritional_values(self):
        self.assertTrue(validate_nutritional_values(self.valid_dish))
        self.assertTrue(validate_nutritional_values(self.high_carb_dish))

    def test_validate_user_height(self):
        self.assertTrue(validate_user_height(50))
        self.assertFalse(validate_user_height(160))
        self.assertFalse(validate_user_height(10))


if __name__ == '__main__':
    unittest.main()
