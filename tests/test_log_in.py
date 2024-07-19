from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import locators


@pytest.mark.parametrize('login_url', [locators.registration_page_url,
                                       locators.forgot_password_page_url,
                                       locators.home_page_url])
def test_log_in_valid_values_logged_in(login_url, log_in, driver):
    login = log_in['login']
    password = log_in['password']
    driver.get(login_url)

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.log_in_elements)))
    driver.find_element(By.XPATH, locators.log_in_elements).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.email_field)))
    driver.find_element(By.XPATH, locators.email_field).send_keys(login)
    driver.find_element(By.XPATH, locators.password_field).send_keys(password)
    driver.find_element(By.XPATH, locators.log_in_elements).click()

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, locators.account_link)))
    driver.find_element(By.XPATH, locators.account_link).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.account_login)))
    login_name = driver.find_element(By.XPATH, locators.account_login).get_attribute('value')
    assert login_name == login


def test_log_in_personal_account_valid_values_logged_in(log_in, driver):
    login = log_in['login']
    password = log_in['password']
    driver.get(locators.home_page_url)

    driver.find_element(By.XPATH, locators.account_link).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.email_field)))
    driver.find_element(By.XPATH, locators.email_field).send_keys(login)
    driver.find_element(By.XPATH, locators.password_field).send_keys(password)
    driver.find_element(By.XPATH, locators.log_in_elements).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
        (By.XPATH, locators.account_link)))
    driver.find_element(By.XPATH, locators.account_link).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.account_login)))
    login_name = driver.find_element(By.XPATH, locators.account_login).get_attribute('value')
    assert login_name == login

    driver.close()
