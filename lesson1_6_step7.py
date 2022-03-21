import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome("webdrivers/chromedriver.exe") as browser:
    browser.get("http://suninjuly.github.io/huge_form.html")
    for text_input in browser.find_elements(By.CSS_SELECTOR, "input"):
        text_input.send_keys("Answer")
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
    time.sleep(30)
