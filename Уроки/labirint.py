from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

driver.maximize_window()
driver.get("https://www.labirint.ru/")

search_locator = "#search-field"

#   искать
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
#   вбивает Python в поиск
search_input.send_keys("Python", Keys.RETURN)

#   собрать карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product")

#   вывести цены

for book in books:
    title = book.find_element(By.CSS_SELECTOR, 'span.product-title').text
    price = book.find_element(By.CSS_SELECTOR, 'span.price-val').text

    author = ''
    try:
        author = book.find_element(By.CSS_SELECTOR, 'div.product-author').text
    except:
        author = 'Автор не указан'

    print(author + "\t" + title + "\t" + price)

sleep(5)
