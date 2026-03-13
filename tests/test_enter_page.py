from pages.recipe_page import RecipePage
import allure


class TestEnterPage:

    @allure.title('Тест на успешную авторизацию и отображение страницы с рецептами после авторизации')
    def test_go_to_main_page_and_displaying_exit_button(self, driver, log_in):
        recipe_page = RecipePage(driver)

        assert (recipe_page.check_displaying_recipes_page() and
                recipe_page.check_displaying_exit_button())
