from selenium.webdriver.common.by import By


class LoginLocators(object):

    LOGIN_BUTTON = (By.CLASS_NAME, "header-profile-icon")
    USERNAME_TEXT_BOX = (By.ID, "LoginEmail")
    PASSWORD_TEXT_BOX = (By.ID, "Password")
    SIGN_IN_BUTTON = (By.ID, "loginLink")


class GeneralLocators(object):

    HOME_PAGE_SELECTOR = (By.CSS_SELECTOR, '.col-sm-12.mb30')
    OPT_IN_DISALLOW = (By.CSS_SELECTOR, '.insider-opt-in-disallow-button')
    CLOSE_POP_UP = (By.ID, 'btnCalcelDeleteCCard')
    BABY_CATEGORY = (By.LINK_TEXT, "BEBEK")
    CATEGORY = (By.XPATH, '/html/body/div[6]/div[2]/div[1]/nav[2]/div[3]/ul/li')


class CategoryPageLocators(object):

    RANDOM_PRODUCT = (By.CLASS_NAME, "featured-item-img")


class ProductPageLocators(object):

    PRODUCT_SIZE = (By.CSS_SELECTOR, 'a[data-stock]:not(.disabled)')
    ADD_TO_CART = (By.CLASS_NAME, 'add-to-cart')


class CartPageLocators(object):

    GO_TO_CHECKOUT = (By.CLASS_NAME, 'btn-checkout')
    REMOVE_ITEM = (By.CLASS_NAME, "sc-delete")
    EMPTY_CART = (By.CLASS_NAME, "shoppingcart-empty")
