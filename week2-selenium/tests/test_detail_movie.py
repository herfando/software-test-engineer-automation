from utils.driver_setup import create_driver
from pages.home_page import HomePage
from pages.detail_page import DetailPage


def test_open_movie_detail():
    driver = create_driver()

    home = HomePage(driver)
    detail = DetailPage(driver)

    # buka home
    home.open()

    # klik movie
    detail.click_first_movie()

    # validasi masuk detail
    assert detail.is_detail_page_loaded()

    print("Detail page berhasil dibuka")

    driver.quit()