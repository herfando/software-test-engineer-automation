from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(BASE_URL + "/home")

    def search_movie(self, keyword):
        search_box = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='Search Movie']")
            )
        )

        print(search_box.get_attribute("outerHTML"))

        search_box.click()
        search_box.clear()
        search_box.send_keys(keyword)