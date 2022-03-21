from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(link_text)

with webdriver.Chrome("webdrivers\chromedriver.exe") as browser:
    browser.get("http://suninjuly.github.io/find_xpath_form")
    browser.find_element("name", "first_name").send_keys("First")
    browser.find_element("name", "last_name").send_keys("Last")
    browser.find_element(By.CLASS_NAME, "form-control.city").send_keys("City")
    browser.find_element("id", "country").send_keys("Country")
    browser.find_element(By.XPATH, "//button[text()=\"Submit\"]").click()
    time.sleep(30)


