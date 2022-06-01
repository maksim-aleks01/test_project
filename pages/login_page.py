from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrationPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' not in current url"# сообщение об ошибке

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is missing"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*RegistrationPageLocators.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*RegistrationPageLocators.INPUT_PASSWORD1).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.INPUT_PASSWORD2).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.REGISTATION_BTN).click()
   