from utils.driver_setup import create_driver


def test_open_movie_app():
    driver = create_driver()

    driver.get("https://movie-app-next-xi.vercel.app/home")

    assert "Create Next App" in driver.title

    print("Movie App berhasil dibuka")

    driver.quit()