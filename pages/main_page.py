from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def transition_to_the_bike_catalog(self):
        """Переход из главного меню в раздел велосипеды"""
        self.logger.info("Переход из главного меню в общий раздел велосипеды")

        main_menu = self.element_is_clickable(self.locators.MAIN_MENU)
        main_menu.click()
        bike_link = self.element_is_clickable(self.locators.BIKE_LINK)
        bike_link.click()
        expected_url = "https://www.sportek.su/catalogue/velosipedy-1.html"
        self.assert_url_to_be(expected_url)

        self.logger.info("Успешно перешли в раздел велосипеды")