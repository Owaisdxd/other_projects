#!/home/os/anaconda3/bin/python

from selenium import webdriver

from selenium.webdriver.common.by import By


# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the test web page
driver.get("http://the-internet.herokuapp.com/javascript_alerts")

# Find the element that triggers the alert and click it

alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")

alert_button.click()

# Switch to alert

alert = driver.switch_to.alert

# Accept the alert

alert.accept()

print("Alert accepted successfully.")

# Dismiss the alert if needed

# alert.dismiss()

# Get text from alert

alert_text = alert.text

print(f"Alert says: {alert_text}")

# Close the browser

driver.quit()
