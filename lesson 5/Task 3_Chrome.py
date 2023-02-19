from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
driver.maximize_window()

#   Открыть страницу:
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#   5 раз кликнуть на кнопку
button = driver.find_element(By.CSS_SELECTOR, "[onclick='addElement()']")
lst = []
for i in range(5):
    button.click()

#   Собрать список кнопок Delete

lst.append(str(driver.find_element(By.CSS_SELECTOR, "button.added-manually")))

print("Размер списка -", len(lst))

driver.close()