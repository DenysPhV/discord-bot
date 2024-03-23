import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def register_user(email, password, confirm_password):
    driver = webdriver.Chrome()
    driver.get("https://tours.seated.com/signup")

    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)

    confirm_password_input = driver.find_element(By.NAME, "passwordConfirm")
    confirm_password_input.send_keys(confirm_password)

    time.sleep(10)

    success_message = driver.find_elements(By.XPATH, "//div[contains(text(), 'Successfully registered')]")

    if success_message:
        driver.quit()
        return True
    else:
        driver.quit()
        return False

