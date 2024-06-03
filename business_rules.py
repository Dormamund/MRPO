from Dish import Dish


def check_dish_carb(dish: Dish) -> bool:
    if dish.carb > 200:
        print(f'Блюдо "{dish.name}"  опасно огромным кол-вом углеводов')
        return True
    else:
        return False


def check_dish_fat(dish: Dish) -> bool:
    if dish.fat > 20:
        print(f'Блюдо "{dish.name}" опасно большим кол-вом жиров')
        return True
    else:
        return False


def validate_nutritional_values(dish: Dish) -> bool:
    if dish.cal < 0 or dish.protein < 0 or dish.fat < 0 or dish.carb < 0:
        print(f'Ошибка: У блюда "{dish.name}" Отрицательная калорийность или БЖУ')
        return False
    return True


def validate_user_height(weight: float) -> bool:
    if 50 <= weight <= 150:
        return True
    else:
        print('Ошибка: Вес пользователя должен быть в диапазоне от 50 до 150 кг.')
        return False


