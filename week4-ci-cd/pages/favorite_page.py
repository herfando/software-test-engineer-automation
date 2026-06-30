from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FavoritePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_favorites(self):
        # asumsi ada nav atau route /favorite
        self.driver.get(BASE_URL + "/favorite")

    def get_favorite_movies(self):
        return self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
        )