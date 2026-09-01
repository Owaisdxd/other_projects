from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument('--headless')  # Run in headless mode

driver = webdriver.Firefox(options=firefox_options)
driver.save_screenshot('screenshot.png')
from time import time

start_time = time()
driver.get('https://www.alnafi.com')
end_time = time()
print(f"Headless Mode Load Time: {end_time - start_time} seconds")

