from pages.enter_page import EnterPage
import allure


class TestCreateAccountPage:

    @allure.title('Тест на отображение страницы авторизации после создания пользователя')
    def test_go_to_auth_page_after_register_and_displaying_form_for_fill_user_data(self, driver, create_user):
        enter_page = EnterPage(driver)

        assert (enter_page.check_displaying_auth_page() and
                enter_page.check_displaying_form_with_user_data())
