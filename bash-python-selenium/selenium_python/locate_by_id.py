from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the HTML test page
driver.get('file:///home/os/Desktop/bash-python-selenium/selenium_python/test_page.html')

# Locate element by ID
username_element = driver.find_element(By.ID,"username")

# Locate element by Name
password_element = driver.find_element(By.Name,"user_password")

# Retrieve and print value
print("Element with Name 'user_password':", password_element.get_attribute('outerHTML'))
# Retrieve and print value
print("Element with ID 'username':", username_element.get_attribute('outerHTML'))

# Close the browser
driver.quit()
