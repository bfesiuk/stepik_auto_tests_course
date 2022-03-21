from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

with webdriver.Chrome("webdrivers/chromedriver.exe") as browser:
    browser.get("http://suninjuly.github.io/selects2.html")
    answer = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    select = Select(browser.find_element(By.CSS_SELECTOR, "select.custom-select"))
    select.select_by_value(str(answer))
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
    time.sleep(20)
