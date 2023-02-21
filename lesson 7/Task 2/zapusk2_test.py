from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.Calculator import Calculator


def test_check_calculator_result():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    calculator = Calculator(browser)
    calculator.delay("45")
    calculator.button()
    sleep(49)
    result = calculator.result()
    assert result == "15"

    browser.quit()

