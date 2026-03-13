from generate_data import GenerateData


class Data(GenerateData):

# Дата рецепта
    def data_for_create_recipe(self):
        return {"name_of_recipe": "Салат из томатов",
                "ingredient": ["помидоры", "лук белый", "соль", "оливковое масло"],
                "count_of_ing": ["200", "50", "7", "10"],
                "time_of_prepare": "30",
                "description": "1. Нарежьте томаты дольками."
                               "2. нарежьте лук полукольцами."
                               "3. Посолите и добавьте оливковое масло."
                               "4. Тщательно перемешайте."
                }


    EMAIL = "example@example.ru" # Постоянный адрес почты
    PASSWORD = "qwerty1111" # Постоянный пароль

    PATH = "assets/tomato_salad_image.jpg" # Путь до фото блюда