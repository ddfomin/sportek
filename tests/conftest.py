import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.logger import get_logger


@pytest.fixture(scope="function")
def driver():
    options = Options()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    # Дополнительные аргументы
    # options.add_argument("--headless")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-password-generation")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def password():
    return "12345678"

@pytest.fixture(scope="function")
def email():
    return "tofejen804@fabaos.com"

@pytest.fixture(scope="function")
def authorization_url():
    return "https://www.sportek.su/login.html"

@pytest.fixture(scope="function")
def logger():
    """Фикстура для логирования в тестах"""
    return get_logger("tests")

