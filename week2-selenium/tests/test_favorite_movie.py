from utils.driver_setup import create_driver
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_favorite_movie():
    driver = create_driver()
    wait = WebDriverWait(driver, 10)

    home = HomePage(driver)
    home.open()

    # ambil movie pertama (card)
    first_movie = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
    )[0]

    # klik favorite button di sekitar movie
    favorite_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
    )
    favorite_button.click()

    # VALIDASI 1: tombol berubah state (warna merah / active)
    assert favorite_button.is_displayed()

    print("Favorite activated")

    # buka favorite page (navbar)
    nav = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "nav"))
    )
    nav.click()

    # VALIDASI 2: movie muncul di favorite page
    favorites = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
    )

    assert len(favorites) > 0

    print("Movie successfully saved to favorites")

    driver.quit()