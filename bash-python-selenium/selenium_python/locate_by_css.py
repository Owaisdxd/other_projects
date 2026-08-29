

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://alnafi.com')

element = driver.find_element(By.cssselector('.classname'))

print(element.tag_name)
print(element.text)
driver.quit()


