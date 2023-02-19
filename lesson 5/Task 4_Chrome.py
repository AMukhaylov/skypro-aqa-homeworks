from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()

#   Открыть страницу:
driver.get("http://uitestingplayground.com/dynamicid")

#   Кликаем на синию кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

for i in range(3):
    blue_button.click()
    print(blue_button.click)
print("Кнопка работает")

driver.close()