from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

RESULT_STR = "Congratulations! You have successfully registered!"


def register(url_link):
    with webdriver.Chrome("webdrivers/chromedriver.exe") as browser:
        browser.implicitly_wait(5)
        browser.get(url_link)

        # input first name
        browser.find_element(By.CSS_SELECTOR, "input[placeholder=\"Input your first name\"]").send_keys("fname")

        # input last name
        browser.find_element(By.CSS_SELECTOR, "input[placeholder=\"Input your last name\"]").send_keys("lname")

        # input email
        browser.find_element(By.CSS_SELECTOR, "input[placeholder=\"Input your email\"]").send_keys("email")

        browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        print(f"{url_link} - {welcome_text}")
        return welcome_text


def test_register_page_1():
    assert register("http://suninjuly.github.io/registration1.html") == RESULT_STR, "Failed result of registration"


def test_register_page_2():
    assert register("http://suninjuly.github.io/registration2.html") == RESULT_STR, "Failed result of registration"


if __name__ == "__main__":
    pytest.main()
