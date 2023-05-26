import time

from selenium.webdriver.common.by import By


class YourCart:
    def __init__(self, driver):
        self.driver = driver

    def remove_backpack(self):
        backpack_remove = self.driver.find_element(By.CSS_SELECTOR, 'button[id="remove-sauce-labs-backpack"]')
        backpack_remove.click()

    def go_to_cart(self):
        cartes = self.driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
        cartes.click()

    def shop(self):
        abcshop= self.driver.find_element(By.XPATH, '//button[@id="continue-shopping"]')
        abcshop.click()

    def checkout(self):
        check = self.driver.find_element(By.CSS_SELECTOR, 'button[id="checkout"]')
        check.click()