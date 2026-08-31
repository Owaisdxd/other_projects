#!/home/os/anaconda3/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("file:///home/os/Desktop/bash-python-selenium/selenium_python/selenium-practice-lab.html")
wait = WebDriverWait(driver, 15)

# --- locators
driver.find_element(By.ID, "locate-by-id")
driver.find_element(By.NAME, "locateByName")
driver.find_element(By.CLASS_NAME, "locate-by-class")
driver.find_element(By.TAG_NAME, "blockquote")
driver.find_element(By.LINK_TEXT, "Jump to the tables section")
driver.find_element(By.PARTIAL_LINK_TEXT, "waits and dynamic")
driver.find_element(By.CSS_SELECTOR, "p.css-target[data-role='css-demo']")
driver.find_element(By.XPATH, "//button[starts-with(@id,'dynamic-btn-')]")

# --- dropdown
Select(driver.find_element(By.ID, "select-single")).select_by_visible_text("Ubuntu 22.04")

# --- explicit wait on late content
driver.find_element(By.ID, "btn-load-late").click()
print(wait.until(EC.visibility_of_element_located((By.ID, "late-content"))).text)

# --- wait for a spinner to go away
driver.find_element(By.ID, "btn-show-spinner").click()
wait.until(EC.invisibility_of_element_located((By.ID, "loading-spinner")))

# --- alert
driver.find_element(By.ID, "btn-prompt").click()
alert = wait.until(EC.alert_is_present())
alert.send_keys("gpu-07")
alert.accept()

# --- iframe
driver.switch_to.frame("simpleFrame")
driver.find_element(By.ID, "frame-input").send_keys("typed inside a frame")
driver.switch_to.default_content()

# --- nested iframe
driver.switch_to.frame("outerFrame")
driver.switch_to.frame("innerFrame")
print(driver.find_element(By.ID, "deep-text").text)
driver.switch_to.default_content()

# --- new tab
original = driver.current_window_handle
driver.find_element(By.ID, "btn-new-tab").click()
wait.until(EC.number_of_windows_to_be(2))
driver.switch_to.window([h for h in driver.window_handles if h != original][0])
driver.close()
driver.switch_to.window(original)

# --- table: state of gpu-02
print(driver.find_element(By.XPATH, "//tr[@id='row-gpu-02']/td[3]").text)

# --- hover menu
menu = driver.find_element(By.ID, "menu-trigger")
ActionChains(driver).move_to_element(menu).perform()
wait.until(EC.visibility_of_element_located((By.ID, "menu-item-drain"))).click()

# --- shadow DOM
root = driver.find_element(By.ID, "shadow-host").shadow_root
root.find_element(By.CSS_SELECTOR, "#shadow-input").send_keys("inside the shadow root")
root.find_element(By.CSS_SELECTOR, "#shadow-button").click()

# --- upload
driver.find_element(By.ID, "file-upload").send_keys("/absolute/path/to/file.txt")

# --- stale element
old = driver.find_element(By.ID, "stale-box")
driver.find_element(By.ID, "btn-make-stale").click()
wait.until(EC.staleness_of(old))
fresh = driver.find_element(By.ID, "stale-box")

# --- login, negative case
driver.find_element(By.ID, "login-username").send_keys("owais")
driver.find_element(By.ID, "login-password").send_keys("wrong" + Keys.ENTER)

assert wait.until(EC.visibility_of_element_located((By.ID, "login-error")))
