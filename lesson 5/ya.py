from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://ya.ru")

# driver.get("https://vk.com")

#    driver.back()
#    driver.forward()
#    driver.refresh()

sleep(15)
