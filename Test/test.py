from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Pages.LoginPage import LoginPage
from Pages.products import product
import time

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)

login_page = LoginPage(driver)
product_page = product(driver)

driver.get("https://www.saucedemo.com/")
login_page.set_username("standard_user")
login_page.set_password("secret_sauce")
login_page.click_login()
time.sleep(3)

product_page.fleece_jacket()
product_page.cart()
time.sleep(10)




