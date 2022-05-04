from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome("webdrivers/chromedriver.exe") as browser:
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/registration2.html")

    # input first name
    browser.find_element(By.CSS_SELECTOR, "input[placeholder=\"Input your first name\"]").send_keys("fname")

    # input last name
    browser.find_element(By.CSS_SELECTOR, "input[placeholder=\"Input your last name\"]").send_keys("lname")

    # input email
    browser.find_element(By.CSS_SELECTOR, "input[placeholder=\"Input your email\"]").send_keys("email")

    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(10)
