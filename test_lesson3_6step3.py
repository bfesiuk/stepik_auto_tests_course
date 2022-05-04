import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


textarea_selector = "textarea.ember-text-area.ember-view.textarea.string-quiz__textarea"
links = ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1", "236903/step/1",
         "236904/step/1", "236905/step/1"]


@pytest.fixture()
def browser():
    browser = webdriver.Chrome("webdrivers/chromedriver.exe")
    browser.implicitly_wait(20)
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_quiz(browser, link):
    browser.get(f"https://stepik.org/lesson/{link}")
    browser.find_element(By.CSS_SELECTOR, textarea_selector).send_keys(str(math.log(int(time.time()))))
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    answer_result = browser.find_element(By.CSS_SELECTOR, "pre.smart-hints__hint").text
    if answer_result != "Correct!":
        with open("l3_6s3.txt", "a") as f:
            f.write(f"{answer_result}\n")
    assert answer_result == "Correct!", f"test in {link} failed! Feedback - {answer_result}"
