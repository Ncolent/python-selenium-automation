from behave import given, when, then
from selenium.webdriver.common.by import By


FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescText')
ORDERS = (By.XPATH, "//span[contains(text(), '& Orders')]")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://amazon.com')
    context.driver.refresh()

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(ORDERS).click()

@when('Open Hamburger Menu')
def open_side_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, 'i.hm-icon').click()

@then('Open Best Sellers Page')
def open_best_sellers_page(context):
    context.driver.find_element(By.CSS_SELECTOR, '[href*="=nav_em_cs_bestsellers_0_1_1"]').click()


@when('Search for {search_word}')
def search_on_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    print(links)
    print(f'Total links:{len(links)}')
    assert len(links) == expected_amount,f'Expected {expected_amount} links but got {len(links)}'


