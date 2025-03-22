from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()  # Initialize Chrome WebDriver
    driver.get("https://www.saucedemo.com/")  # Open the website
    driver.maximize_window()

    # Locate input fields and login button
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Perform login action
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Wait for the page to load
    time.sleep(3)

    # Verify successful login by checking if the products page is displayed
    assert "inventory.html" in driver.current_url, "Login failed!"

    # Close the browser
    driver.quit()
