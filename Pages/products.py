from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class product:
    def __init__(self,driver):
        self.driver = driver


    def fleece_jacket(self):
        f_jacket = self.driver.find_element(By.CSS_SELECTOR, 'button[ id="add-to-cart-sauce-labs-fleece-jacket"]')
        f_jacket.click()


    def cart(self):
        c_at = self.driver.find_element(By.CSS_SELECTOR, 'span[class="shopping_cart_badge"]')
        c_at.click()





# def class_filter(self, filter_by):
#     WebDriverWait(self.driver, 10).until(
#         EC.presence_of_element_located(self.filter)
#     )
#     Select = Select(self.driver.find_element(*self.filter))
#     Select.select_by_value(filter_by)



