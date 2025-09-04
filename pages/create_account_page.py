from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators
from generate_data import GenerateData
import allure


class CreateAccountPage(BasePage):

    @allure.step('Заполнение поля имени')
    def fill_input_first_name(self):
        generate_data = GenerateData()

        self.fill_input(RegisterPageLocators.NAME_INPUT, generate_data.create_name())

    @allure.step('Заполнение поля фамилии')
    def fill_input_last_name(self):
        generate_data = GenerateData()

        self.fill_input(RegisterPageLocators.SURNAME_INPUT, generate_data.create_last_name())

    @allure.step('Заполнение поля имени пользователя')
    def fill_input_username(self):
        generate_data = GenerateData()

        self.fill_input(RegisterPageLocators.USER_NAME_INPUT, generate_data.create_user_name())

    @allure.step('Клик по кнопке создания пользователя')
    def click_to_button_create_user(self):
        self.click_to(RegisterPageLocators.BUTTON_CREATE_ACCOUNT)

    @allure.step('Заполнение поля пароль')
    def fill_password_input(self, password):
        self.fill_input(RegisterPageLocators.PASSWORD_INPUT, password)

    @allure.step('Заполнение поля адрес почты')
    def fill_email_input(self, email):
        self.fill_input(RegisterPageLocators.ADDRESS_INPUT, email)