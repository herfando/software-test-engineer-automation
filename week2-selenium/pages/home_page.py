from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://movie-app-next-xi.vercel.app/home")

    def search_movie(self, keyword):
        search_box = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search Movie']"))
        )
        search_box.click()
        search_box.send_keys(keyword)