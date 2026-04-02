from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def login(self, email, password):
        """Авторизация (ввод логина и пароля, подтверждение)"""

        self.logger.info("Начинаем авторизацию")

        email_input = self.element_is_clickable(self.locators.EMAIL_INPUT)
        password_input = self.element_is_clickable(self.locators.PASSWORD_INPUT)
        enter_button = self.element_is_clickable(self.locators.ENTER_BUTTON)

        email_input.clear()
        email_input.send_keys(email)
        self.logger.debug("Ввели логин/почту")

        password_input.clear()
        password_input.send_keys(password)
        self.logger.debug("Ввели пароль")

        enter_button.click()
        self.logger.debug("Нажали кнопку для входа")

        expected_url = "https://www.sportek.su/"
        self.assert_url_to_be(expected_url)

        self.logger.info("Авторизация прошла успешно")

