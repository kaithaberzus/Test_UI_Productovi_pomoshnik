from pages.recipe_page import RecipePage
import allure


class TestRecipePage:

    @allure.title('Тест на успешное добавление карточки рецепта и названия рецепта после его создания')
    def test_create_recipe(self, driver, log_in):
        recipe_page = RecipePage(driver)

        recipe_page.click_to_create_recipe_button()
        recipe_page.add_new_ing(0)
        recipe_page.add_new_ing(1)
        recipe_page.add_new_ing(2)
        recipe_page.add_new_ing(3)
        recipe_page.fill_all_fields()
        recipe_page.send_photo_of_dish()
        recipe_page.click_submit_recipe_button()

        assert (recipe_page.check_displaying_name_of_recipe_is_true()
                and recipe_page.check_displaying_recipe_card_in_line())
