from locators import *
from base_functions import BaseFunctions
import parameters


class ProductPageFunctions(BaseFunctions):

    def __init__(self, driver):
        self.driver = driver
        self.base_functions = BaseFunctions()

    def pick_size(self):

        self.base_functions.wait_method(self.driver, ProductPageLocators.PRODUCT_SIZE).click()

    def add_to_cart(self):
        self.wait_method(self.driver, ProductPageLocators.ADD_TO_CART)
        self.base_functions.wait_method(self.driver, ProductPageLocators.ADD_TO_CART).click()

    def go_to_cart(self):

        self.driver.get(parameters.CART_URL)


