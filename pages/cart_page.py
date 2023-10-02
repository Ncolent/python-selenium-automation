from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class CartPage(Page):
    EMPTY_CART = (By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty")
    CART_BTTN = (By.ID, 'nav-cart')
    ADD_TO_CART = (By.ID, 'add-to-cart-button')
    PRODUCT_NAME = (By.ID, 'productTitle')
    PRODUCT_ADDED_TO_CART = (By.ID, '.a-size-medium-plus')

    def click_cart(self):
        self.click(*self.CART_BTTN)

    def verify_empty_cart(self, string):
        self.verify_text(string, *self.EMPTY_CART)

    def verify_product_added(self, expected_text):
        self.verify_text(expected_text, *self.PRODUCT_ADDED_TO_CART)

    def verify_product_correct(self, expected_text):
        self.verify_text(expected_text, *self.PRODUCT_NAME)

