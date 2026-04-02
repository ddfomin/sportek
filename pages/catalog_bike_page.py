from random import randint
from locators.catalog_bike_page_locators import CatalogBikePageLocators
from locators.select_type_bike_page_locators import SelectTypeBikePageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.select_type_bike_page import SelectTypeBikePage


class CatalogBikePage(BasePage):
    locators = CatalogBikePageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.type_bike = SelectTypeBikePage(driver)
        self.type_bike_locators = SelectTypeBikePageLocators()
        self.main = MainPage(driver)

    def select_random_type_bike(self):
        """Выбор случайного типа велосипеда с товарами"""
        attempt = 0

        while True:
            attempt += 1
            type_bikes = self.elements_are_clickable(self.locators.TYPE_BIKES)

            if len(type_bikes) == 0:
                self.logger.error("Типы велосипедов не найдены")
                return False

            # Выбираем случайный тип
            random_index = randint(0, len(type_bikes) - 1)
            type_bikes[random_index].click()
            name_type = self.element_is_visible(self.type_bike_locators.NAME_TYPE_BIKE).text
            self.logger.info(f"Попытка {attempt}: выбран тип: {name_type}")

            # Если товары есть - выходим из цикла
            if not self.type_bike.check_empty_message():
                self.logger.info(f"У найденного типа присутствуют товары")
                break

            self.logger.info("Товары не найдены, пробуем другой тип")
            self.main.transition_to_the_bike_catalog()

        return True






