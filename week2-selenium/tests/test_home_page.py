from utils.driver_setup import create_driver


def test_home_page_load():
    driver = create_driver()

    driver.get("https://movie-app-next-xi.vercel.app/home")

    assert "Create Next App" in driver.title

    print("Home page loaded successfully")

    driver.quit()