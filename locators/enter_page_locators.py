from selenium.webdriver.common.by import By


class EnterPageLocators:

    # Локатор кнопки создания пользователя
    BUTTON_CREATE_USER = By.XPATH, ".//a[text()='Создать аккаунт']"

    # Локатор поля ввода адреса почты
    ADDRESS_INPUT = By.NAME, "email"

    # Локатор поля ввода пароля
    PASSWORD_INPUT = By.NAME, "password"

    # Локатор кнопки входа
    BUTTON_ENTER = By.TAG_NAME, "button"

    # Локатор формы с данными пользователя
    FORM_USER_DATA = By.XPATH, ".//form[@class='styles_form__2nwxz styles_form__2_42b']"