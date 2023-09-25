from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
PRODUCT_LINK = (By.CSS_SELECTOR, "[href*='-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1']")
driver.wait = WebDriverWait(driver,10)



@then('Verify search result is {expected_result}')
def verify_search_result(context,expected_result):
    actual_result = context.driver.find_element(SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error expected {expected_result} did not match actual {actual_result}'

@then('Select Product')
def select_product(context):
    context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_LINK)).click()





