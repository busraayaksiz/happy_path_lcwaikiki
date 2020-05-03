from locators import *
from base_functions import BaseFunctions
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class CartPageFunctions(BaseFunctions):

    def __init__(self, driver):
        self.driver = driver
        self.base_functions = BaseFunctions()

    def go_to_checkout(self):

        self.base_functions.wait_method(self.driver, CartPageLocators.GO_TO_CHECKOUT).click()

    def remove_items_from_cart(self):

        self.base_functions.wait_method(self.driver, CartPageLocators.REMOVE_ITEM).click()
        try:
            self.assert_empty_cart()
        except TimeoutException:
            self.remove_items_from_cart()

    def assert_empty_cart(self):
        assert self.base_functions.wait_method(self.driver, CartPageLocators.EMPTY_CART).is_displayed, True
