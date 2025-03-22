import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture(scope="module")
def driver():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver  # Provides the driver instance to the test functions
    driver.quit()  # Close the browser after all tests are done

def test_login(driver):
    driver.get("https://www.saucedemo.com/")  # Open the website

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
    
def test_add_to_cart(driver):
    # Locate the first product and add it to the cart
    first_product = driver.find_element(By.CLASS_NAME, "inventory_item")
    add_to_cart_button = first_product.find_element(By.CLASS_NAME, "btn_inventory")
    add_to_cart_button.click()

    # Wait for the item to be added to the cart
    time.sleep(2)

    # Verify that the product was added to the cart
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "1", f"Expected 1 item in the cart, but found {cart_count}"

def test_checkout(driver):
    # Navigate to the cart page
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    # Wait for the cart page to load
    time.sleep(3)

    # Click the checkout button
    checkout_button = driver.find_element(By.CLASS_NAME, "checkout_button")
    checkout_button.click()

    # Fill out the checkout form
    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_code_input = driver.find_element(By.ID, "postal-code")

    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")
    postal_code_input.send_keys("12345")

    # Proceed to the next step
    continue_button = driver.find_element(By.CLASS_NAME, "cart_button")
    continue_button.click()

    # Wait for the checkout page to load
    time.sleep(3)

    # Verify that the checkout page is displayed
    assert "checkout-step-two.html" in driver.current_url, "Checkout failed!"