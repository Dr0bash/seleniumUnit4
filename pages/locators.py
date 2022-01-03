from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_PRODUCTS_CONTAINER = (By.CLASS_NAME, "basket-items")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_FORM_EMAIL = (By.ID, "id_registration-email")
    REGISTER_FORM_PASS = (By.ID, "id_registration-password1")
    REGISTER_FORM_PASS_REPEAT = (By.ID, "id_registration-password2")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, ".btn-primary[name='registration_submit']")

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    TITLE_TEXT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_TITLE_LABEL = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner strong")
    ALERT_PRICE_LABEL = (By.CSS_SELECTOR, "#messages :nth-child(3) .alertinner strong")
    