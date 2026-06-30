from base_test import BaseTest

class TestHomePage(BaseTest):

    def test_home_page_load(self):
        self.driver.get("https://movie-app-next-xi.vercel.app/home")

        assert "Create Next App" in self.driver.title

        print("Home page loaded successfully")