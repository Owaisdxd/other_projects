from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.save_screenshot('headless_ss.png')
driver.quit()
