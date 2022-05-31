from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        self.should_be_product_name()
        self.should_be_price()

    #Метод проверки соответствия наименновани добавленного товара в коризну и сообщения об успешно добавленном товаре
    def should_be_product_name(self):
        product_name_el = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name_el.text
        expected_result_el = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        expected_result = expected_result_el.text 
        assert expected_result == product_name, "Product name is wrong!!!"
    
    def should_be_price(self):
        product_price_el = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price_el.text
        expected_result_el = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
        expected_result = expected_result_el.text
        assert expected_result == product_price, "Product price is wrong!!!"