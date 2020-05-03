from locators import *
from base_functions import *
from selenium.webdriver.common.by import By
import time


class HomePageFunctions(BaseFunctions):

    def __init__(self, driver):
        self.driver = driver
        self.base_functions = BaseFunctions()

    def allow_optin(self):
        self.base_functions.wait_method(self.driver, (By.CLASS_NAME, 'insider-opt-in-allow-button')).click()

    def home_page_assertion(self):
        home_page = self.base_functions.wait_method(self.driver, GeneralLocators.HOME_PAGE_SELECTOR).is_displayed()
        assert home_page, True

    def go_to_login_page(self):
        self.base_functions.wait_method(self.driver, LoginLocators.LOGIN_BUTTON).click()

    """def close_phone_popup(self):
        time.sleep(1)
        pop_up_displayed = self.base_functions.wait_method(self.driver, GeneralLocators.CLOSE_POP_UP).is_displayed()
        while pop_up_displayed:
            self.base_functions.wait_method(self.driver, GeneralLocators.CLOSE_POP_UP).click()
            break"""

    def go_to_category_page(self):

        self.wait_method(self.driver, GeneralLocators.CATEGORY)
        selector = GeneralLocators.CATEGORY
        random_value = self.driver.find_elements(*selector)
        rand_value = random_value[randint(0, len(random_value) - 1)]
        rand_value.click()


