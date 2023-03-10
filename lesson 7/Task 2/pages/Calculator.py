from selenium.webdriver.common.by import By


class Calculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay(self, time: str):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time)

    def button(self):
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
        self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(4)').click()
        self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(2)').click()
        self._driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()

    def result(self):
        end_result = self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.top > div').text
        return end_result
