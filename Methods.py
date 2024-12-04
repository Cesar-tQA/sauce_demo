from selenium.webdriver.common.by import By
import Data


class SauceDemoPage:
    #Locators
    page_name = (By.ID, 'user-name')
    page_password = (By.ID, 'password')
    login_button = (By.ID, 'login-button')
    sauce_labs_backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
    sauce_labs_bike_light = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    sauce_labs_bolt_tshirt = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    sauce_labs_fleece_jacket = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    sauce_labs_onesie = (By.ID, 'add-to-cart-sauce-labs-onesie')
    pay_car = (By.CLASS_NAME, 'shopping_cart_link')
    total_pay = (By.ID, 'checkout')

    def __init__(self, driver):
        self.driver = driver

    def get_user(self):
        return self.driver.find_element(*self.page_name).get_property('value')

    def get_password(self):
        return self.driver.find_element(*self.page_password).get_property('value')

    #Those methods find the user and user password field

    def set_user(self):
        user_field = self.driver.find_element(*self.page_name)
        user_field.click()
        user_field.send_keys(Data.user_name)

    def set_password(self):
        password_field = self.driver.find_element(*self.page_password)
        password_field.click()
        password_field.send_keys(Data.password)

    def click_login_button(self):
        login = self.driver.find_element(*self.login_button)
        login.click()

    def click_sauce_labs_backpack(self):
        labs_backpack = self.driver.find_element(*self.sauce_labs_backpack)
        labs_backpack.click()

    def click_to_sauce_labs_bike_light(self):
        labs_bike_light = self.driver.find_element(*self.sauce_labs_bike_light)
        labs_bike_light.click()

    def click_to_sauce_labs_bolt_tshirt(self):
        labs_bolt_tshirt = self.driver.find_element(*self.sauce_labs_bolt_tshirt)
        labs_bolt_tshirt.click()

    def click_to_sauce_labs_fleece_jacket(self):
        labs_fleece_jacket = self.driver.find_element(*self.sauce_labs_fleece_jacket)
        labs_fleece_jacket.click()

    def click_to_sauce_labs_onesie(self):
        labs_onesie = self.driver.find_element(*self.sauce_labs_onesie)
        labs_onesie.click()

    def click_to_pay_car(self):
        pay_cart = self.driver.find_element(*self.pay_car)
        pay_cart.click()

    def click_to_total_pay(self):
        checkout = self.driver.find_element(*self.total_pay)
        checkout.click()
    #Those methods prepare to click on the locators and design the test