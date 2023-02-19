from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()

#   Открыть страницу:
driver.get("http://uitestingplayground.com/classattr")

#   Кликаем на синию кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary.btn-test")

for i in range(3):
    blue_button.click()
    sleep(1)
    Alert(driver).accept()
print("Кнопка работает")

sleep(3)
driver.close()