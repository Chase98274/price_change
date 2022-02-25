import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
  executable_path='C:\\Users\\chase\\Documents\\price_change\\chromedriver.exe') 
driver.get('https://www.100percent.co.nz/')


# driver.implicitly_wait(10)
driver.maximize_window()

searchElement = driver.find_element(By.ID, "searchterm")
searchElement.send_keys("bbm450an")
searchElement.send_keys(Keys.ENTER)

model = driver.find_element(By.CSS_SELECTOR, "p.style-number").text
print("Text is: " + model)

price = driver.find_element(By.CSS_SELECTOR, "p.price").text
print("Price: " + price)

driver.close()
