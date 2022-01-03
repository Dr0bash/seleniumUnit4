from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasketPage(BasePage):
    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS_CONTAINER), \
           "Success message is presented, but should not be"

    def should_be_message_about_empty_basket(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert "Ваша корзина пуста" in empty_basket_message.text, "There is no empty basket message"