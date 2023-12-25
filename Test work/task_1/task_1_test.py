from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

wait = WebDriverWait(driver, 20)

driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")
driver.find_element(By.TAG_NAME, "button").click()

red_color = 'rgba(248, 215, 218, 1)'
green_color = 'rgba(209, 231, 221, 1)'
new_list = [driver.find_element(By.ID, "first-name").value_of_css_property('background-color'),
            driver.find_element(By.ID, "last-name").value_of_css_property('background-color'),
            driver.find_element(By.ID, "address").value_of_css_property('background-color'),
            driver.find_element(By.ID, "e-mail").value_of_css_property('background-color'),
            driver.find_element(By.ID, "phone").value_of_css_property('background-color'),
            driver.find_element(By.ID, "city").value_of_css_property('background-color'),
            driver.find_element(By.ID, "country").value_of_css_property('background-color'),
            driver.find_element(By.ID, "job-position").value_of_css_property('background-color'),
            driver.find_element(By.ID, "company").value_of_css_property('background-color')]


def test_red_color():
    Zip_code = driver.find_element(By.ID, "zip-code")
    assert Zip_code.value_of_css_property('background-color') == red_color, "Не подсвечено красным"

def test_green_color():
    for element in new_list:
        assert element == green_color, "Поля не подсвечены зеленым"