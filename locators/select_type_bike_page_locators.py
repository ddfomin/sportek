class SelectTypeBikePageLocators:

    # Локаторы для настройки фильтров
    LEFT_SLIDER = ("xpath", "(//span[contains(@class, 'ui-slider-handle')])[1]")
    CHECKBOX_IN_STOCK = ("xpath", "//div[@id='available_0-styler']")
    SELECT_PARAMETERS_BUTTON = ("xpath", "//input[@value='Подобрать']")

    # Локаторы первого из списка велосипеда
    ADD_BUTTON_FIRST_BIKE = ("xpath", "(//button[contains(@class, 'btn_cart add-product-to-cart')])[1]")
    NAME_FIRST_BIKE = ("xpath", "//*[@id='yw0']/div[2]/div[1]/div[3]/a")
    PRICE_FIRST_BIKE = ("xpath", "(//span[@class='result-price-value'])[1]")
    BUY_BUTTON_FOR_FIRST_BIKE = ("xpath", "//a[@class='button']")

    # Прочие локаторы
    EMPTY_MESSAGE = ("xpath", "//span[@class='empty']")
    NAME_TYPE_BIKE = ("xpath", "//h1")