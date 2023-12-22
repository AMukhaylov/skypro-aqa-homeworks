from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://uitestingplayground.com/textinput")

waiter = WebDriverWait(driver, 30)

driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro"))

print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)