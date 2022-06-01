from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BUSKET_MSG = (By.CSS_SELECTOR, "#content_inner > p")