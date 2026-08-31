#!/home/os/anaconda3/bin/python

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time


    # Initialize WebDriver and launch a website
    driver = webdriver.Chrome()
    driver.get("https://amazon.ae")
    time.sleep(5)
    link = driver.find_elements(By.XPATH, "/html/body/div[1]/header/div/div[5]/div[2]/div/div/ul/li[1]/div/a")
    time.sleep(5)
    link.click()
except Exception as e:
    print("Check this error", e)
