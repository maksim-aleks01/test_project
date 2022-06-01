from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        link.click()

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEM), "Basket in not empty!!!"
        assert self.is_element_present(*BasePageLocators.EMPTY_BUSKET_MSG), "Missing 'empty basket' message!!!"
