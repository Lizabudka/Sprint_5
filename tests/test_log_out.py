from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


def test_log_out_from_personal_account_logged_out(driver, log_in):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.account_link)))
    driver.find_element(By.XPATH, locators.account_link).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.log_out_button)))
    driver.find_element(By.XPATH, locators.log_out_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.log_in_text)))
    assert driver.find_element(By.XPATH, locators.log_in_text)
