from selenium.webdriver.common.by import By


class RecipePageLocators:

    # Локатор поля ввода названия рецепта
    INPUT_NAME_OF_RECIPE = By.XPATH, ".//div[text()='Название рецепта']/../input"

    # Локатор поля ввода ингредиента
    INPUT_TYPE_OF_ING = By.XPATH, ".//input[@class='styles_inputField__3eqTj styles_ingredientsInput__1zzql']"

    # Локатор поля ввода количества ингредиента
    INPUT_COUNT_OF_ING = By.XPATH, ".//input[@class='styles_inputField__3eqTj styles_ingredientsAmountValue__2matT']"

    # Локатор поля ввода времени приготовления
    INPUT_TIME_OF_PREPARE = By.XPATH, ".//div[text()='Время приготовления']/../input"

    # Локатор поля ввода описания рецепта
    INPUT_DESCRIPTION_OF_RECIPE = By.XPATH, ".//textarea[@class='styles_textareaField__1wfhC']"

    # Локатор кнопки перехода на страницу создания рецепта
    BUTTON_CREATE_AN_RECIPE = By.XPATH, ".//a[@href='/recipes/create']"

    # Локатор кнопки выхода
    BUTTON_EXIT = By.XPATH, ".//a[text()='Выход']"

    # Локатор страницы создания рецепта
    RICEPIES_PAGE = By.XPATH, ".//h1[text()='Рецепты']"

    # Локатор кнопки добавления ингредиента
    BUTTON_ADD_ING = By.XPATH, ".//div[contains(@class, 'styles_ingredientAdd') and text()='Добавить ингредиент']"

    # Локатор кнопки создания рецепта
    BUTTON_SUBMIT_RECIPE = By.XPATH, "//button[contains(@class, 'styles_button') and contains(text(), 'Создать рецепт')]"

    # Локатор кнопки добавления фото блюда
    ADD_PHOTO = By.XPATH, "//input[@type='file' and contains(@class, 'styles_fileInput')]"

    # Локатор Первого в списке ингредиента
    FIRST_IN_LIST_OF_ING = By.XPATH, ".//div[@class='styles_container__3ukwm']/div[1]"