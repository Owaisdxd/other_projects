#!/home/os/anaconda3/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.amazon.ae/")

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    print(">>>",link.text, link.get_attributes('href'))

driver.quit()
