from data.data_generator import get_random_user
from locators.cart_page_locators import CartPageLocators
from pages.base_page import BasePage


class CardPage(BasePage):
    locators = CartPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def get_parameters_product(self):
        """Получение параметров товара в корзине"""
        self.logger.debug("Получение параметров товара в корзине")
        name_bike = self.element_is_visible(self.locators.NAME_BIKE).text
        price_bike = self.element_is_visible(self.locators.PRICE_BIKE).text
        count_bike = self.element_is_visible(self.locators.COUNT_BIKE).get_attribute("value")
        total_price = self.element_is_visible(self.locators.TOTAL_PRICE).text
        self.logger.info(f"В корзине «{name_bike}» за {price_bike} руб. в количестве {count_bike} шт. Итоговая цена = {total_price} руб.")

        return name_bike, price_bike, total_price

    def fill_personal_data(self):
        """Заполнение персональных данных"""
        self.logger.info("Начинаем заполнять персональные данные")
        # Сгенерировали персональные данные
        data = get_random_user()

        # Заполняем персональные данные
        fio = self.element_is_clickable(self.locators.FIO)
        self.go_to_element(fio)
        fio.clear()
        fio.send_keys(data["full_name"])
        self.logger.info("Заполнили ФИО")

        phone_number = self.element_is_clickable(self.locators.PHONE_NUMBER)
        phone_number.clear()
        phone_number.send_keys(data["phone_number"])
        self.logger.info("Заполнили номер телефона")

        email = self.element_is_clickable(self.locators.EMAIL)
        email.clear()
        email.send_keys(data["email"])
        self.logger.info("Заполнили почту")

        delivery_method = self.element_is_clickable(self.locators.DELIVERY_METHOD_3)
        delivery_method.click()
        self.logger.info("Выбрали метод доставки: Доставка транспортной компанией")

        comment = self.element_is_clickable(self.locators.COMMENT)
        comment.clear()
        comment.send_keys(data["comment"])
        self.logger.info("Заполнили комментарий")

        address_delivery = self.element_is_clickable(self.locators.ADDRESS_DELIVERY)
        address_delivery.send_keys(data["address"])
        self.logger.info("Заполнили адрес доставки")

    def check_button_buy(self):
        """Проверка возможности оформления заказа. Отмечаем чек-бокс на обработку персональных данных, проверяем кнопку Оформить"""
        checkbox_order_rule = self.element_is_clickable(self.locators.ORDER_RULE)

        if not checkbox_order_rule.is_selected():
            checkbox_order_rule.click()
            self.logger.info("Отметили чек-бокс на согласие с условиями обработки персональных данных")
        else:
            self.logger.info("Чек-бокс на согласие с условиями обработки персональных данных уже отмечен")

        button_buy = self.element_is_clickable(self.locators.BUTTON_PLACE_AN_ORDER)
        self.logger.info("Кнопка «Оформить» активна, но нажимать не будем")
