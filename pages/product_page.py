from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not presented"

    def should_be_right_price(self):
        price_label = self.browser.find_element(*ProductPageLocators.PRICE_TEXT)
        alert_price_label = WebDriverWait(self.browser, 12).until(
            EC.presence_of_element_located(ProductPageLocators.ALERT_PRICE_LABEL)
        )
        assert alert_price_label.text == price_label.text, "Price is not equal"

    def should_be_right_title(self):
        title_label = self.browser.find_element(*ProductPageLocators.TITLE_TEXT)
        alert_title_label = WebDriverWait(self.browser, 12).until(
            EC.presence_of_element_located(ProductPageLocators.ALERT_TITLE_LABEL)
        )
        assert alert_title_label.text == title_label.text, "Title is not equal"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_TITLE_LABEL), \
           "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_TITLE_LABEL), \
           "Success message is presented, but should not be"
