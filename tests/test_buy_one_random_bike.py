from pages.cart_page import CardPage
from pages.catalog_bike_page import CatalogBikePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.select_type_bike_page import SelectTypeBikePage


def test_buy_random_bike(driver, authorization_url, email, password, logger):
    """Тест на покупку одного случайного велосипеда. Автотест выбирает случайный тип велосипеда, у которого
    присутствуют товары. Далее выставляет случайные фильтры и добавляет первый товар из списка. После переходит к оформлению
    заказа, сверяет название и цену добавленного товара, заполняет данные покупателя случайными значениями и проверяет
    возможность оформления"""

    logger.info("Запуск теста на покупку одного случайного велосипеда")
    # Авторизация
    login_page = LoginPage(driver, authorization_url)
    login_page.open()
    login_page.login(email, password)

    # Переход в каталог велосипедов
    main_page = MainPage(driver)
    main_page.transition_to_the_bike_catalog()

    # Выбор случайного типа велосипеда с товарами
    catalog_page = CatalogBikePage(driver)
    catalog_page.select_random_type_bike()

    # Добавление товара в корзину
    select_bike_page = SelectTypeBikePage(driver)
    select_bike_page.setting_random_filters()
    name, price = select_bike_page.get_bike()
    select_bike_page.go_to_card()

    # Оформление заказа
    cart_page = CardPage(driver)
    name_bike, price_bike, total_price = cart_page.get_parameters_product()

    assert name == name_bike, "Названия товара отличаются (каталог - корзина)"
    assert price == price_bike, "Цена отличается (каталог - корзина)"
    assert total_price == price, "Цена за товар и итоговая цена отличаются"

    cart_page.fill_personal_data()
    cart_page.check_button_buy()

    logger.info("Тест пройден")