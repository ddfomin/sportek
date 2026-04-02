from random import randint
from locators.select_type_bike_page_locators import SelectTypeBikePageLocators
from pages.base_page import BasePage


class SelectTypeBikePage(BasePage):
    locators = SelectTypeBikePageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def check_empty_message(self):
        """Проверка наличия сообщения 'Нет результатов.'"""
        return self.element_is_visible_not_raise(self.locators.EMPTY_MESSAGE)

    def setting_random_filters(self):
        """Настройка фильтров (случайный выбор цены) пока не найдутся товары"""
        self.logger.info("Начинаем настройку фильтров")

        max_attempts = 10

        # Устанавливаем чек-бокс "В наличии"
        checkbox_in_stock = self.element_is_clickable(self.locators.CHECKBOX_IN_STOCK)
        if not checkbox_in_stock.is_selected():
            checkbox_in_stock.click()
            self.logger.debug("Установили чек-бокс 'В наличии'")

        attempt = 0
        while attempt < max_attempts:
            attempt += 1
            self.logger.debug(f"Попытка {attempt} из {max_attempts}")

            try:
                # Перемещаем ползунок цены
                left_slider = self.element_is_clickable(self.locators.LEFT_SLIDER)
                random_num = randint(0, 200)
                self.action_drag_and_drop_by_offset(left_slider, random_num, 0)
                self.logger.debug(f"Переместили левый ползунок на {random_num} пикселей")

                # Нажимаем кнопку "Подобрать"
                select_button = self.element_is_clickable(self.locators.SELECT_PARAMETERS_BUTTON)
                select_button.click()
                self.logger.debug("Нажали кнопку 'Подобрать'")

                # Проверяем, есть ли товары
                if not self.element_is_visible_not_raise(self.locators.EMPTY_MESSAGE, timeout=2):
                    self.logger.info(f"Фильтры применились успешно с {attempt} попытки")
                    return True
                else:
                    self.logger.warning(f"Попытка {attempt}: товары не найдены")

                    # Возвращаем ползунок назад
                    left_slider = self.element_is_clickable(self.locators.LEFT_SLIDER)
                    self.action_drag_and_drop_by_offset(left_slider, -random_num, 0)

                    # Применяем фильтры после отката
                    select_button = self.element_is_clickable(self.locators.SELECT_PARAMETERS_BUTTON)
                    select_button.click()

            except Exception as e:
                self.logger.error(f"Попытка {attempt}: ошибка {e}")
                continue

        self.logger.error(f"Не удалось найти товары после {max_attempts} попыток")
        return False

    def get_bike(self):
        """Добавление в корзину велосипеда"""
        self.logger.debug("Будем добавлять первый велосипед из списка в корзину")
        name_bike = self.element_is_visible(self.locators.NAME_FIRST_BIKE).text
        price_bike = self.element_is_visible(self.locators.PRICE_FIRST_BIKE).text
        self.logger.info(f"Выбрали первый из списка велосипед: «{name_bike}». Цена: {price_bike} руб.")

        add_button = self.element_is_clickable(self.locators.ADD_BUTTON_FIRST_BIKE)
        add_button.click()
        self.logger.info(f"Велосипед был добавлен в корзину")

        return name_bike, price_bike

    def go_to_card(self):
        """Переход в корзину"""
        self.logger.debug("Будем переходить на страницу оформления заказа")
        buy_button = self.element_is_clickable(self.locators.BUY_BUTTON_FOR_FIRST_BIKE)
        buy_button.click()
        self.logger.debug("Клик на кнопку 'Оформить заказ'")

        expected_url = "https://www.sportek.su/cart.html"
        self.assert_url_to_be(expected_url)

        self.logger.info("Перешли на форму корзины/оформления заказа")