from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()

#   Открыть страницу:
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)

#   В модальном окне нажать на кнопку Close
button_close = driver.find_element(By.CSS_SELECTOR, "div.modal-footer > p")
button_close.click()

sleep(1)
driver.close()