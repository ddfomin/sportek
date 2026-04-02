from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import Screenshot
from utils.logger import get_logger


class BasePage:

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.screenshot = Screenshot(driver)
        self.logger = get_logger(self.__class__.__name__)
        self.logger.debug(f"Инициализация страницы: {self.__class__.__name__}")

    # ==================== Навигация ====================

    def open(self):
        """Открытие URL в браузере"""
        self.logger.debug(f"Открываем URL: {self.url}")
        self.driver.get(self.url)

    # ==================== Ожидание элементов ====================

    def element_is_visible(self, locator, timeout=10):
        """Ожидание видимости элемента"""
        self.logger.debug(f"Ожидание видимости элемента: {locator}")
        try:
            return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            self.logger.error(f"Элемент не стал видимым: {locator}")
            raise

    def element_is_visible_not_raise(self, locator, timeout=10):
        """Ожидание видимости элемента без обработки try/except"""
        try:
            wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def elements_are_visible(self, locator, timeout=10):
        """Ожидание видимости элементов"""
        self.logger.debug(f"Ожидание видимости элементов: {locator}")
        try:
            return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except Exception as e:
            self.logger.error(f"Элементы не стали видимыми: {locator}")
            raise

    def element_is_present(self, locator, timeout=10):
        """Ожидание присутствия элемента в DOM"""
        self.logger.debug(f"Ожидание присутствия элемента: {locator}")
        try:
            return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            self.logger.error(f"Элемент не появился в DOM: {locator}")
            raise

    def elements_are_present(self, locator, timeout=10):
        """Ожидание присутствия элементов в DOM"""
        self.logger.debug(f"Ожидание присутствия элементов: {locator}")
        try:
            return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except Exception as e:
            self.logger.error(f"Элементы не появились в DOM: {locator}")
            raise

    def element_is_not_visible(self, locator, timeout=10):
        """Ожидание невидимости элемента"""
        self.logger.debug(f"Ожидание невидимости элемента: {locator}")
        try:
            return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except Exception as e:
            self.logger.error(f"Элемент все еще видим: {locator}")
            raise

    def element_is_clickable(self, locator, timeout=10):
        """Ожидание кликабельности элемента"""
        self.logger.debug(f"Ожидание кликабельности элемента: {locator}")
        try:
            return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            self.logger.error(f"Элемент не стал кликабельным: {locator}")
            raise

    def elements_are_clickable(self, locator, timeout=10):
        """Ожидание кликабельности всех элементов"""
        self.logger.debug(f"Ожидание кликабельности элементов: {locator}")
        try:
            return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except Exception as e:
            self.logger.error(f"Элементы не стали кликабельными: {locator}")
            raise

    # ==================== Работа с элементами ====================

    def go_to_element(self, element):
        """Скролл к элементу"""
        self.logger.debug("Скролл к элементу")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # ==================== Работа с окнами ====================

    def switch_to_new_window(self, number):
        """Переключение на окно или вкладку по индексу"""
        self.logger.debug(f"Переключение на окно с индексом {number}")
        self.driver.switch_to.window(self.driver.window_handles[number])

    # ==================== Action Chains ====================

    def action_double_click(self, element):
        """Двойной клик по элементу"""
        self.logger.debug("Двойной клик")
        try:
            action = ActionChains(self.driver)
            action.double_click(element)
            action.perform()
            self.logger.debug("Двойной клик выполнен успешно")
        except Exception as e:
            self.logger.error(f"Ошибка при двойном клике: {e}")
            self.screenshot.get_screenshot()
            raise

    def action_right_click(self, element):
        """Правый клик по элементу"""
        self.logger.debug("Правый клик")
        try:
            action = ActionChains(self.driver)
            action.context_click(element)
            action.perform()
            self.logger.debug("Правый клик выполнен успешно")
        except Exception as e:
            self.logger.error(f"Ошибка при правом клике: {e}")
            self.screenshot.get_screenshot()
            raise

    def action_drag_and_drop_by_element(self, what, where):
        """Перетаскивание одного элемента на другой"""
        self.logger.debug("Drag and drop на элемент")
        try:
            action = ActionChains(self.driver)
            action.drag_and_drop(what, where)
            action.perform()
            self.logger.debug("Drag and drop выполнен успешно")
        except Exception as e:
            self.logger.error(f"Ошибка при drag and drop: {e}")
            self.screenshot.get_screenshot()
            raise

    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        """Перетаскивание элемента по координатам"""
        self.logger.debug(f"Drag and drop по координатам: ({x_coords}, {y_coords})")
        try:
            action = ActionChains(self.driver)
            action.drag_and_drop_by_offset(element, x_coords, y_coords)
            action.perform()
            self.logger.debug("Drag and drop выполнен успешно")
        except Exception as e:
            self.logger.error(f"Ошибка при drag and drop: {e}")
            self.screenshot.get_screenshot()
            raise

    def action_move_to_element(self, element):
        """Наведение курсора на элемент"""
        self.logger.debug("Наведение курсора")
        try:
            action = ActionChains(self.driver)
            action.move_to_element(element)
            action.perform()
            self.logger.debug("Наведение курсора выполнено успешно")
        except Exception as e:
            self.logger.error(f"Ошибка при наведении курсора: {e}")
            self.screenshot.get_screenshot()
            raise

    def action_click_and_hold(self, element):
        """Клик и удержание элемента"""
        self.logger.debug("Клик и удержание элемента")
        try:
            action = ActionChains(self.driver)
            action.click_and_hold(element)
            action.perform()
            self.logger.debug("Клик и удержание выполнены успешно")
        except Exception as e:
            self.logger.error(f"Ошибка при клике и удержании: {e}")
            self.screenshot.get_screenshot()
            raise

    def action_release(self):
        """Отпускание удерживаемой кнопки мыши"""
        self.logger.debug("Отпускание кнопки мыши")
        try:
            action = ActionChains(self.driver)
            action.release()
            action.perform()
            self.logger.debug("Кнопка мыши отпущена успешно")
        except Exception as e:
            self.logger.error(f"Ошибка при отпускании кнопки мыши: {e}")
            self.screenshot.get_screenshot()
            raise

    # ==================== Проверка URL ====================

    def assert_url_to_be(self, url, timeout=10):
        """Проверка, что текущий URL соответствует ожидаемому"""
        self.logger.debug(f"Ожидание URL: {url}")
        try:
            wait(self.driver, timeout).until(EC.url_to_be(url))
            self.logger.debug(f"Успешный переход на URL: {url}")
        except Exception as error:
            self.screenshot.get_screenshot()
            self.logger.error(f"Переход не произошел. Ожидалось: {url}, Текущий: {self.driver.current_url}")
            raise AssertionError(
                f"Переход не произошел. Ожидалось: {url}, "
                f"Текущий: {self.driver.current_url}"
            )

    def get_current_url(self):
        """Получение текущего URL"""
        current_url = self.driver.current_url
        self.logger.debug(f"Текущий URL: {current_url}")
        return current_url