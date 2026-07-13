from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pymysql

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

time.sleep(5)

input_name = driver.find_element(By.ID,"username")
input_name.send_keys("student")
input_passwd = driver.find_element(By.ID,"password")
input_passwd.send_keys("Password123")
submit_me = driver.find_element(By.ID,"submit")
submit_me.click()
time.sleep(10)
driver.quit()

conn = pymysql.connect(
        host='database_identifier',
        user='admin',
        password='Admin123',
        database='my_test_db'
)
cursor = conn.cursor()

createl_table_query = """
       CREATE TABLE IF NOT EXISTS form_submissions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255)
          )
"""
cursor.execute(createl_table_query)

sql = "INSERT INTO form_submissions (username, password) VALUES (%s, %s)"
values = ("student", "admin123")
cursor.execute(sql, values)
conn.commit()
conn.close()

