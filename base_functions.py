from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from random import randint


class BaseFunctions(object):

    def wait_method(self, driver, selector):
        return WebDriverWait(driver, 10).until(ec.element_to_be_clickable(selector))

