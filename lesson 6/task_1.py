from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://uitestingplayground.com/ajax")

waiter = WebDriverWait(driver, 30)

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content > p"), "Data loaded with AJAX get request."))

print(driver.find_element(By.CSS_SELECTOR, "#content").text)
