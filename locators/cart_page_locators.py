class CartPageLocators:

    # Параметры товара в корзине
    NAME_BIKE = ("xpath", "//a[@class='cart-item__link']")
    PRICE_BIKE = ("xpath", "//span[@class='position-price']")
    COUNT_BIKE = ("xpath", "//input[@class='position-count']")
    TOTAL_PRICE = ("xpath", "//span[@id='cart-full-cost-with-shipping']")

    # Персональные данные
    FIO = ("xpath", "//input[@id='Order_name']")
    PHONE_NUMBER = ("xpath", "//input[@id='Order_phone']")
    EMAIL = ("xpath", "//input[@id='Order_email']")
    DELIVERY_METHOD_3 = ("xpath", "//div[@id='delivery-3-styler']")
    ADDRESS_DELIVERY = ("xpath", "//textarea[@id='Order_address']")
    COMMENT = ("xpath", "//textarea[@id='Order_comment']")

    # Чек-бокс на согласие с условиями обработки, кнопка оформить заказ
    ORDER_RULE = ("xpath", "//div[contains(@class, 'jq-checkbox input')]")
    BUTTON_PLACE_AN_ORDER = ("xpath", "//button[@type='submit']")