import Dish
import Diary
import Diet
import Ingredient
import User


user1 = User.User(1, 20, 'муж', 80, 'Влад', 'низкая')
user2 = User.User(2, 21, 'муж', 65, 'Дмитрий', 'высокая')
user3 = User.User(3, 21, 'муж', 72, 'Иван', 'средняя')

ingredient1 = Ingredient.Ingredient('Филе курицы')
ingredient2 = Ingredient.Ingredient('Картофель')
ingredient3 = Ingredient.Ingredient('Помидоры')
ingredient4 = Ingredient.Ingredient('Макароны')
ingredient5 = Ingredient.Ingredient('Яйца')
ingredient6 = Ingredient.Ingredient('Клубника')

diet1 = Diet.Diets('Низкокаллорийная')
diet2 = Diet.Diets('Кето-диета')
diet3 = Diet.Diets('Белковая')


dish1 = Dish.Dish(1, 'Вареная курица и пару долек помидоров', 987, 84, 12, 69, {ingredient1: 200, ingredient3: 150}, diet1)
dish2 = Dish.Dish(2, 'Вареные яйца с клубникой', 560, 99, 100, 2, {ingredient5: 240, ingredient6: 400}, diet2)

diary1 = Diary.Diary(1, user1, 'Завтрак', dish1.name)
diary2 = Diary.Diary(2, user2, 'Обед', dish2.name)
diary3 = Diary.Diary(3, user1, 'Ужин', dish1.name)


