from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url is not right"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
        
    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        reg_pass = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS)
        reg_pass_rep = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS_REPEAT)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
        reg_email.send_keys(email)
        reg_pass.send_keys(password)
        reg_pass_rep.send_keys(password)
        reg_button.click()