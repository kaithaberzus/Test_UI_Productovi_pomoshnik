from selenium.webdriver.common.by import By


class RegisterPageLocators:

    # Локатор поля ввода имени
    NAME_INPUT = By.NAME, "first_name"

    # Локатор поля ввода фамилии
    SURNAME_INPUT = By.NAME, "last_name"

    # Локатор поля ввода имя пользователя
    USER_NAME_INPUT = By.NAME, "username"

    # Локатор поля ввода адреса почты
    ADDRESS_INPUT = By.NAME, "email"

    # Локатор поля ввода пароля
    PASSWORD_INPUT = By.NAME, "password"

    # Локатор кнопки создания аккаунта
    BUTTON_CREATE_ACCOUNT = By.XPATH, "//button[contains(@class, 'styles_button') and contains(text(), 'Создать аккаунт')]"