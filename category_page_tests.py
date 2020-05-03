from locators import *
from base_functions import *
import  random

class CategoryPageFunctions(BaseFunctions):


    def __init__(self, driver):
        self.driver = driver
        self.base_functions = BaseFunctions()

    def click_random_product(self):
        self.wait_method(self.driver, CategoryPageLocators.RANDOM_PRODUCT)
        product_list = self.driver.find_elements(*CategoryPageLocators.RANDOM_PRODUCT)
        product = random.randint(0, len(product_list) - 1)
        product_list[product].click()
