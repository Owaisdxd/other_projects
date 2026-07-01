from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pymysql

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

time.sleep(5)

