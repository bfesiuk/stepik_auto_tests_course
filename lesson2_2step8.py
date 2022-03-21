from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import time

file_path = Path.joinpath(Path(__file__).resolve().parent, "lesson2_2_step8.txt")
print(file_path)
with webdriver.Chrome("webdrivers/chromedriver.exe") as browser:
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.CSS_SELECTOR, "input[name=firstname").send_keys("firstname")
    browser.find_element(By.CSS_SELECTOR, "input[name=lastname]").send_keys("lastname")
    browser.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("email")
    browser.find_element(By.CSS_SELECTOR, "input#file").send_keys(rf"{file_path}")
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(20)
