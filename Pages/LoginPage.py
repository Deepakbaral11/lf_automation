from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.XPATH, "//input[@id='user-name']")
        self.password_field = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//input[@id='login-button']")

    def set_username(self, user_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username)
        )
        self.driver.find_element(*self.username).send_keys(user_name)

    def set_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)
        )
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        self.driver.find_element(*self.login_button).click()
