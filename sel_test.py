from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Runs Chrome without a GUI
chrome_options.add_argument("--no-sandbox")     # Bypasses OS security model (required for Jenkins)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://aws.amazon.com/")
print(driver.title)
time.sleep(5)
driver.quit()

