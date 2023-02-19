from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()

#   Открыть страницу:
driver.get('http://the-internet.herokuapp.com/inputs')
sleep(1)

#   Введите в поле текст 1000
search = driver.find_element(By.CSS_SELECTOR, "[type='number']")
search.send_keys("1000")
sleep(1)

#   Очистите это поле, метод Clear
search.clear()
sleep(1)

#   Введите в это же поле текст SkyPro (данное поле не принимает буквы)
search.send_keys("777")

sleep(1)
driver.close()