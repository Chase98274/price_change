import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector

models = ["bbm450an", "bbm450w", "bvf290w", "NEX110DFSL", "dfhfshkjhfsdkjhfsdjk", "WAX32M41AU"]
na = []

def write_data(code, price):
  try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Hayman_Robyn577",
            database="product_info")

        mySql_insert_query = "INSERT INTO products (code, price) VALUES (%s, %s)"
        data = (code, price)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, data)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into info table")
        cursor.close()

  except mysql.connector.Error as error:
      print("Failed to insert record into info table {}".format(error))

  finally:
      if connection.is_connected():
          connection.close()
          print("MySQL connection is closed")


driver = webdriver.Chrome(
  executable_path='C:\\Users\\chase\\Documents\\price_change\\chromedriver.exe') 
driver.get('https://www.100percent.co.nz/')


# driver.implicitly_wait(10)
driver.maximize_window()

def price_product():
  searchElement = driver.find_element(By.ID, "searchterm")
  searchElement.send_keys(item)
  searchElement.send_keys(Keys.ENTER)

  model = driver.find_element(By.CSS_SELECTOR, "p.style-number").text
  print("Text is: " + model)

  price = driver.find_element(By.CSS_SELECTOR, "p.price").text
  print("Price: " + price)

  write_data(model, price)

  driver.find_element(By.ID, "searchterm").clear()

for item in models: 

  try:
    price_product()

  except:
    na.append(item)
    driver.find_element(By.ID, "searchterm").clear()


for item in na:
  print("{} was unavailable".format(item))

driver.close()