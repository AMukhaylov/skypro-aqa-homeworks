from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()

#   Открыть страницу:
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

#   В поле username ввести значение "tomsmith"
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")
sleep(2)

#   В поле password ввести значение "SuperSecretPassword!"
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")
sleep(2)

#   Нажать на кнопку "Login"
button_login = driver.find_element(By.CSS_SELECTOR, ".fa")
button_login.click()

sleep(2)
driver.close()