from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    TITLE_TEXT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_TITLE_LABEL = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")
    ALERT_PRICE_LABEL = (By.CSS_SELECTOR, "#messages :nth-child(3) .alertinner strong")
    