from locators import *
from base_functions import BaseFunctions


class LoginPageFunctions(BaseFunctions):

    def __init__(self, driver):
        self.driver = driver
        self.base_functions = BaseFunctions()

    def login(self, mail, password):

        self.base_functions.wait_method(self.driver, LoginLocators.USERNAME_TEXT_BOX).send_keys(mail)
        self.base_functions.wait_method(self.driver, LoginLocators.PASSWORD_TEXT_BOX).send_keys(password)
        self.base_functions.wait_method(self.driver, LoginLocators.SIGN_IN_BUTTON).click()
