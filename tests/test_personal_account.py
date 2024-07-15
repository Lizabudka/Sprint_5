from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


def test_click_on_personal_account_when_logged_in_transmit_to_personal_account(driver, log_in):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.account_link)))
    driver.find_element(By.XPATH, locators.account_link).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains('profile'))
    assert driver.current_url == locators.account_page_url


def test_click_on_personal_account_when_not_logged_transmit_to_login_page(driver):
    driver.get(locators.home_page_url)

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.account_link)))
    driver.find_element(By.XPATH, locators.account_link).click()

    WebDriverWait(driver, 5).until(expected_conditions.url_contains('login'))
    assert driver.current_url == locators.login_page_url
