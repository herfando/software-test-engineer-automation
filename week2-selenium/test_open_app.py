from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()

driver = webdriver.Chrome(options=options)

driver.get("https://movie-app-next-xi.vercel.app/home")

print(driver.title)

input("Tekan Enter untuk menutup browser...")

driver.quit()