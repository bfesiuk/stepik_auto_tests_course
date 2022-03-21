from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

with webdriver.Chrome("webdrivers/chromedriver.exe") as browser:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary").click()
    browser.switch_to.window(browser.window_handles[1])
    x_value = int(browser.find_element(By.CSS_SELECTOR, "span#input_value").text)
    math_result = math.log(math.fabs(12*math.sin(x_value)))
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(math_result)
    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(20)
