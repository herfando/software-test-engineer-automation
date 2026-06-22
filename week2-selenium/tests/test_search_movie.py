from utils.driver_setup import create_driver
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_movie():
    driver = create_driver()

    home = HomePage(driver)

    # buka halaman
    home.open()

    # lakukan search
    home.search_movie("the")

    # VALIDASI hasil search
    wait = WebDriverWait(driver, 10)

    movies = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img"))
    )

    assert len(movies) > 0

    print(f"Search berhasil, ditemukan {len(movies)} movie")

    driver.quit()