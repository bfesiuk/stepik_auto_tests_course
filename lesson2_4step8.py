from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

with webdriver.Chrome("webdrivers/chromedriver.exe") as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    book_btn = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100"))
    browser.find_element(By.CSS_SELECTOR, "button#book").click()
    x_value = int(browser.find_element(By.CSS_SELECTOR, "span#input_value").text)
    math_result = math.log(math.fabs(12*math.sin(x_value)))
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(math_result)
    browser.find_element(By.CSS_SELECTOR, "button#solve").click()
    time.sleep(20)
