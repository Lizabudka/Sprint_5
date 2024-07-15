from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


def test_click_on_constructor_from_personal_account_transition_to_main_page(driver, log_in):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.account_link)))
    driver.find_element(By.XPATH, locators.account_link).click()

    WebDriverWait(driver, 5).until((expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.logo_link))))
    driver.find_element(By.XPATH, locators.logo_link).click()

    assert driver.current_url == locators.home_page_url


def test_click_on_logo_from_personal_account_transition_to_main_page(driver, log_in):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.account_link)))
    driver.find_element(By.XPATH, locators.account_link).click()

    WebDriverWait(driver, 5).until((expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.constructor_link))))
    driver.find_element(By.XPATH, locators.constructor_link).click()

    assert driver.current_url == locators.home_page_url
