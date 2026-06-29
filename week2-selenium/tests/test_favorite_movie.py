from base_test import BaseTest
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFavoriteMovie(BaseTest):

    def test_favorite_movie(self):
        wait = WebDriverWait(self.driver, 10)

        home = HomePage(self.driver)
        home.open()

        first_movie = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
        )[0]

        favorite_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
        )
        favorite_button.click()

        assert favorite_button.is_displayed()

        print("Favorite activated")

        nav = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "nav"))
        )
        nav.click()

        favorites = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
        )

        assert len(favorites) > 0

        print("Movie successfully saved to favorites")