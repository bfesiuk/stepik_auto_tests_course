from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

with webdriver.Chrome("webdrivers/chromedriver.exe") as browser:
    browser.get("https://suninjuly.github.io/execute_script.html")
    x_value = int(browser.find_element(By.CSS_SELECTOR, "span#input_value").text)
    math_result = math.log(math.fabs(12*math.sin(x_value)))
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(math_result)
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_btn)
    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()
    submit_btn.click()
    time.sleep(20)
