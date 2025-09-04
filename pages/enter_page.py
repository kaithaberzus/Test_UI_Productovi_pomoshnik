from locators.enter_page_locators import EnterPageLocators
from pages.base_page import BasePage
import config
import allure


class EnterPage(BasePage):

    @allure.step('Заполнение поля адреса почты')
    def fill_input_email(self, email):
        self.fill_input(EnterPageLocators.ADDRESS_INPUT, email)

    @allure.step('Заполнение поля пароля')
    def fill_input_password(self, password):
        self.fill_input(EnterPageLocators.PASSWORD_INPUT, password)

    @allure.step('Клик по кнопке входа')
    def click_to_enter_button(self):
        self.click_to(EnterPageLocators.BUTTON_ENTER)

    @allure.step('Открытие главной страницы')
    def open_base_url(self):
        self.open_url(config.MAIN_PAGE, EnterPageLocators.BUTTON_ENTER)

    @allure.step('Клик по кнопке перехода на страницу создания аккаунта')
    def click_to_create_account_button_in_enter_page(self):
        self.click_to(EnterPageLocators.BUTTON_CREATE_USER)

    @allure.step('Проверка отображения страницы авторизации')
    def check_displaying_auth_page(self):
        return self.check_displaying(EnterPageLocators.BUTTON_ENTER)

    @allure.step('Проверка отображения формы для авторизации')
    def check_displaying_form_with_user_data(self):
        return self.check_displaying(EnterPageLocators.FORM_USER_DATA)