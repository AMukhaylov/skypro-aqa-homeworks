from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, 20)

# Авторизация
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

# Добавление товара в корзину
driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.NAME,"add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.NAME,"add-to-cart-sauce-labs-onesie").click()

# Оформление заказа
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
driver.find_element(By.ID,"checkout").click()
driver.find_element(By.ID,"first-name").send_keys("Артур")
driver.find_element(By.ID,"last-name").send_keys("Мухайлов")
driver.find_element(By.ID,"postal-code").send_keys(7777)
driver.find_element(By.ID,"continue").click()

# Читаем со страницы итоговую стоимость
total_price = driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container")
text = total_price.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_info_label.summary_total_label").text

# Закрываем браузер
driver.quit()
def test_total_price():
    assert text == "Total: $58.29", "Не такая сумма сформировалась"