import os
from datetime import datetime

def get_screenshots_dir():
    """Получить путь к папке со скриншотами"""
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "reports", "screenshots"
    )

def clear_screenshots():
    """Очистить папку со скриншотами"""
    dir_path = get_screenshots_dir()

    if os.path.exists(dir_path):
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("Скриншоты удалены")


class Screenshot:
    def __init__(self, driver):
        self.driver = driver

    def get_screenshot(self):
        dir_path = get_screenshots_dir()
        os.makedirs(dir_path, exist_ok=True)

        timestamp = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        file_path = os.path.join(dir_path, f"screenshot_{timestamp}.png")

        self.driver.save_screenshot(file_path)

if __name__ == "__main__":
    clear_screenshots()