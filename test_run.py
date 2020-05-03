import unittest
from home_page_tests import *
from login_page_tests import *
from category_page_tests import *
from product_page_tests import *
from cart_page_tests import *
from selenium import webdriver
from base_functions import BaseFunctions
import parameters


class TestRun(unittest.TestCase, BaseFunctions):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.home_page_tests = HomePageFunctions(driver=self.driver)
        self.login_page_tests = LoginPageFunctions(driver=self.driver)
        self.category_page_tests = CategoryPageFunctions(driver=self.driver)
        self.product_page_tests = ProductPageFunctions(driver=self.driver)
        self.cart_page_tests = CartPageFunctions(driver=self.driver)
        self.driver.get(parameters.TEST_URL)

    def test(self):

        self.home_page_tests.home_page_assertion()
        self.home_page_tests.go_to_login_page()
        self.login_page_tests.login(parameters.MAIL, parameters.PASSWORD)
        self.home_page_tests.go_to_category_page()
        self.category_page_tests.click_random_product()
        self.product_page_tests.pick_size()
        self.product_page_tests.add_to_cart()
        self.product_page_tests.go_to_cart()
        self.cart_page_tests.go_to_checkout()
        self.product_page_tests.go_to_cart()
        self.cart_page_tests.remove_items_from_cart()

    def TearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
