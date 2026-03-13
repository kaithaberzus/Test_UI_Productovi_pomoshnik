from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.create_account_page import CreateAccountPage
from generate_data import GenerateData
from data import Data
from pages.enter_page import EnterPage


# Фикстура создания драйвера для хрома
@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Фикстура создания пользователя
@pytest.fixture()
def create_user(driver):
    create_account_page = CreateAccountPage(driver)
    enter_page = EnterPage(driver)
    generate_data = GenerateData()

    email = generate_data.create_email()
    password = generate_data.create_password()

    enter_page.open_base_url()
    enter_page.click_to_create_account_button_in_enter_page()
    create_account_page.fill_email_input(email)
    create_account_page.fill_password_input(password)
    create_account_page.fill_input_username()
    create_account_page.fill_input_last_name()
    create_account_page.fill_input_first_name()
    create_account_page.click_to_button_create_user()

    yield  email, password

# Фикстура логина
@pytest.fixture()
def log_in(driver):
    enter_page = EnterPage(driver)

    enter_page.open_base_url()
    enter_page.fill_input_email(Data.EMAIL)
    enter_page.fill_input_password(Data.PASSWORD)
    enter_page.click_to_enter_button()

    return
