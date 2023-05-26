from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#chrome_driver_path = 'D:/automation/chromedriver.exe'
#driver = 'D:/automation/chromedriver.exe'
# Open Swag labs website
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# For login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(3)
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(3)
driver.find_element(By.ID, "login-button").click()
time.sleep(3)
print(driver.title)


#Return back to the login page
driver.back()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

# selecting Price high to low from dropdown
dropdown = driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
dd = Select(dropdown)

# select by visible text
dd.select_by_visible_text('Price (high to low)')
time.sleep(3)
print('set item to high to low')

driver.find_element(By.NAME, 'add-to-cart-sauce-labs-fleece-jacket').click()
time.sleep(3)
item2 = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
print('item added to cart')


# Now add to Cart (By using css selector)
driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()
driver.find_element(By.ID,'checkout').click()
driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Deepak')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Baral')
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('4800')

print(driver)
driver.find_element(By.CSS_SELECTOR, '#continue').click()
time.sleep(5)
driver.find_element(By.ID, 'finish').click()
print('Progress completed')


expected_text = 'CHECKOUT: COMPLETE!'
actual_text = driver.find_element(By.XPATH,"//span[@class='title']").text
#assert expected_text == actual_text, f'error'
#assert expected_text == actual_text, f'Error, Expected text:{expected_text}, but actual text: {actual_text}'
assert expected_text == actual_text, f', Expected text:{expected_text}, but actual text: {actual_text}'


#Quitting the browser
driver.quit()