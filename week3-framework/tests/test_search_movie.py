from base_test import BaseTest
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearchMovie(BaseTest):

    def test_search_movie(self):
        home = HomePage(self.driver)

        home.open()
        home.search_movie("the")

        wait = WebDriverWait(self.driver, 10)

        movies = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
        )

        assert len(movies) > 0

        print(f"Search berhasil, ditemukan {len(movies)} movie")