from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


def test_registration_valid_data_registration_complited(registration, driver, random_login, random_password):
    login = random_login
    password = random_password

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.registration_link)))
    driver.find_element(By.XPATH, locators.registration_link).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.name_field)))
    driver.find_element(By.XPATH, locators.name_field).send_keys('Test')
    driver.find_element(By.XPATH, locators.email_field).send_keys(login)
    driver.find_element(By.XPATH, locators.password_field).send_keys(password)
    driver.find_element(By.XPATH, locators.registration_button).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.new_user_error_text)))
    assert driver.find_element(By.XPATH, locators.new_user_error_text).text


def test_registration_4_digit_password_incorrect_password_error(random_login, driver):
    random_login = random_login
    driver.get(locators.home_page_url)

    driver.find_element(By.XPATH, locators.account_link).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.registration_link)))
    driver.find_element(By.XPATH, locators.registration_link).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.name_field)))
    driver.find_element(By.XPATH, locators.name_field).send_keys('Test')
    driver.find_element(By.XPATH, locators.email_field).send_keys(random_login)
    driver.find_element(By.XPATH, locators.password_field).send_keys('1234')
    driver.find_element(By.XPATH, locators.registration_button).click()

    assert 'Некорректный пароль' == driver.find_element(By.XPATH, locators.incorrect_password_error_text).text
