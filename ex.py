from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://kite.zerodha.com/")

# Wait for the username input field to be visible
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))

# Find the username and password input fields and enter the values
password_field = driver.find_element(By.NAME, "password")
username_field.send_keys("your_username")
password_field.send_keys("your_password")

# Find the login button and click it
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()