from selenium.webdriver.common.by import By


class RecipeCardPageLocators:

    # Локатор карточки рецепта
    CRAD = By.XPATH, ".//div[@class='styles_single-card__1yTTj']"

    # Локатор названия рецепта в карточке
    NAME_OF_RECIPE_IN_CARD = By.XPATH, ".//h1[@class='styles_single-card__title__2QMPq']"