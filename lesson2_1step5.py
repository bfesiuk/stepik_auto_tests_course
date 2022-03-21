from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

with webdriver.Chrome("webdrivers/chromedriver.exe") as browser:
    browser.get("http://suninjuly.github.io/math.html")
    x_value = int(browser.find_element(By.CSS_SELECTOR, "span[id=input_value]").text)
    math_result = math.log(math.fabs(12*math.sin(x_value)))
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(math_result)
    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
    time.sleep(20)
