from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_first_movie(self):
        # ambil semua movie card (pakai img sebagai awal)
        movies = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
        )

        # klik movie pertama
        movies[0].click()

    def is_detail_page_loaded(self):
        # validasi sederhana: URL berubah atau ada konten detail
        return "/movie" in self.driver.current_url or "/detail" in self.driver.current_url