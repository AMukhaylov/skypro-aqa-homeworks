from selenium.webdriver.common.by import By


class Magazine:
    def __init__(self, driver, url: str):
        self._driver = driver
        self._driver.get(url)

    def username(self, username: str):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)

    def password(self, password: str):
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

    def button(self, locator):
        self._driver.find_element(By.CSS_SELECTOR, locator).click()

    def post(self):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Test")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Testovich")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("777")

    def price(self):
        txt = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        return txt

