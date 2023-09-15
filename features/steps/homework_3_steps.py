from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://amazon.com')
    sleep(2)
    context.driver.refresh()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.XPATH, "//span[contains(text(), '& Orders')]").click()

@then('Verify Sign-in page is opened')
def verify_sign_in(context):
    expected_result = 'Sign In'
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]")
    assert expected_result == actual_result, f'Error expected {expected_result} did not match actual {actual_result}'