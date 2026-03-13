from locators.create_recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage
from locators.recipe_card_page_locators import RecipeCardPageLocators
from data import Data
import allure


class RecipePage(BasePage):

    @allure.step('Заполнение поля названия рецепта')
    def fill_input_name_of_recipe(self):
        data = Data()

        self.fill_input(RecipePageLocators.INPUT_NAME_OF_RECIPE, data.data_for_create_recipe()['name_of_recipe'])

    @allure.step('Заполнение поля названия ингредиента')
    def fill_input_type_of_ingredients(self, num):
        data = Data()

        self.fill_input(RecipePageLocators.INPUT_TYPE_OF_ING, data.data_for_create_recipe()['ingredient'][num])

    @allure.step('Заполнение поля количества ингредиента')
    def fill_input_count_of_ingredient(self, num):
        data = Data()

        self.fill_input(RecipePageLocators.INPUT_COUNT_OF_ING, data.data_for_create_recipe()['count_of_ing'][num])

    @allure.step('Заполнение поля времени приготовления')
    def fill_input_time_of_prepare(self):
        data = Data()

        self.fill_input(RecipePageLocators.INPUT_TIME_OF_PREPARE, data.data_for_create_recipe()['time_of_prepare'])

    @allure.step('Заполнение поля описания рецепта')
    def fill_input_description(self):
        data = Data()

        self.fill_input(RecipePageLocators.INPUT_DESCRIPTION_OF_RECIPE, data.data_for_create_recipe()['description'])

    @allure.step('Клик по кнопке перехода на страницу создания рецепта')
    def click_to_create_recipe_button(self):
        self.click_to(RecipePageLocators.BUTTON_CREATE_AN_RECIPE)

    @allure.step('Клик по кнопке добавления ингредиента')
    def click_to_add_ing_button(self):
        self.click_to(RecipePageLocators.BUTTON_ADD_ING)

    @allure.step('Клик по кнопке создания рецепта')
    def click_submit_recipe_button(self):
        self.click_to(RecipePageLocators.BUTTON_SUBMIT_RECIPE)

    @allure.step('Клик по первому ингредиенту из списка')
    def click_to_ing_in_list(self):
        self.click_to(RecipePageLocators.FIRST_IN_LIST_OF_ING)

    @allure.step('Проверка отображения карточки рецепта')
    def check_displaying_recipe_card_in_line(self):
        return self.check_displaying(RecipeCardPageLocators.CRAD)

    @allure.step('Проверка совпадения названия созданного рецепта с названием в карточке')
    def check_displaying_name_of_recipe_is_true(self):
        return self.get_text_from_element(RecipeCardPageLocators.NAME_OF_RECIPE_IN_CARD) == 'Салат из томатов'

    @allure.step('Отправка фото блюда')
    def send_photo_of_dish(self):
        data = Data()

        self.upload_image(data.PATH, RecipePageLocators.ADD_PHOTO)

    @allure.step('Проверка отображения страницы с рецептами')
    def check_displaying_recipes_page(self):
        return self.check_displaying(RecipePageLocators.RICEPIES_PAGE)

    @allure.step('Проверка отображения кнопки выхода')
    def check_displaying_exit_button(self):
        return self.check_displaying(RecipePageLocators.BUTTON_EXIT)

    @allure.step('Добавление нового ингредиента')
    def add_new_ing(self, num):
        self.fill_input_type_of_ingredients(num)
        self.click_to_ing_in_list()
        self.fill_input_count_of_ingredient(num)
        self.click_to_add_ing_button()

    @allure.step('Заполнение всех полей для создания рецепта')
    def fill_all_fields(self):
        self.fill_input_name_of_recipe()
        self.fill_input_time_of_prepare()
        self.fill_input_description()
