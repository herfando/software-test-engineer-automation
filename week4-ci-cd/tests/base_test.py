from selenium import webdriver


class BaseTest:

    def setup_method(self):
        self.driver = webdriver.Chrome()

        self.driver.set_window_size(1280, 800)

    def teardown_method(self):
        self.driver.quit()