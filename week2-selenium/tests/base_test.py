from utils.driver_setup import create_driver

class BaseTest:

    def setup_method(self):
        self.driver = create_driver()

    def teardown_method(self):
        self.driver.quit()