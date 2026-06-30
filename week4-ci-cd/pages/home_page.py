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

        # 🔥 STEP 1: klik icon search MOBILE (Vector3.png)
        search_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='search']"))
        )
        search_icon.click()

        # 🔥 STEP 2: tunggu input mobile muncul (setelah state berubah)
        search_box = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder='Search Movie']")
            )
        )

        search_box.clear()
        search_box.send_keys(keyword)