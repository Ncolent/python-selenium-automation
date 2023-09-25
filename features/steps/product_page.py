from behave import given, when, then
from selenium.webdriver.common.by import By

ADD_TO_CART = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, 'li[id*=color_name]')
CURRENT_COLOR = (By.CSS_SELECTOR, '.selection')



@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

@then('Add product to cart')
def add_product_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()

@when("Store Product Name")
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')

@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = COLOR_OPTIONS

    colors = context.driver.find_element(*COLOR_OPTIONS)
    print(colors)
    print(len(colors))

    for color in colors:
        color.click()