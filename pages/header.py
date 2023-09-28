from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTTN = (By.ID, 'nav-search-submit-button')
    ORDER_BUTTON = (By.ID, 'nav-orders')



    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTTN)

    def click_orders_link(self):
        self.click(*self.ORDER_BUTTON)


