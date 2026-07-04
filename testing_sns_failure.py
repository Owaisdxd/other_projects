from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import boto3

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
try:
    element=driver.find_element(By.ID,"username1")
    print("Element found")
except:
    print("Element NotFound. Test Failed")
driver.quit()

#SeleniumTestFailed

