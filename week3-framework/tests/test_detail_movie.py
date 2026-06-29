from base_test import BaseTest
from pages.home_page import HomePage
from pages.detail_page import DetailPage

class TestDetailMovie(BaseTest):

    def test_open_movie_detail(self):
        home = HomePage(self.driver)
        detail = DetailPage(self.driver)

        home.open()
        detail.click_first_movie()

        assert detail.is_detail_page_loaded()

        print("Detail page berhasil dibuka")