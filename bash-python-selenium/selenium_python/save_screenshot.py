#!/home/os/anaconda3/bin/python

from selenium import webdriver

import time 

driver = webdriver.Chrome()

driver.get("https://www.alnafi.com")

#screenshot_file  = "screenshot.png"

#driver.save_screenshot(screenshot_file)

timestamp = time.strftime("%Y-%m-%d-%H:%M:%S")

timestamped_file = f"screenshot_{timestamp}.png"

driver.save_screenshot(timestamped_file)

