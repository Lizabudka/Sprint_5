from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import random
import string
import locators

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

@pytest.fixture(scope='function')
def random_login():
    random_letters = random.choices(string.ascii_letters, k=3)
    r_login = ''.join(random_letters) + str(random.randint(0000, 9999)) + '@ya.ru'
    return r_login


@pytest.fixture(scope='function')
def random_password():
    r_password = str(random.randint(000000, 999999))
    return r_password


@pytest.fixture(scope='function')
def registration(random_login, random_password, driver):

    driver.get(locators.registration_page_url)

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((
        By.XPATH, locators.name_field)))
    driver.find_element(By.XPATH, locators.name_field).send_keys('Test')
    driver.find_element(By.XPATH, locators.email_field).send_keys(random_login)
    driver.find_element(By.XPATH, locators.password_field).send_keys(random_password)
    driver.find_element(By.XPATH, locators.registration_button).click()


@pytest.fixture(scope='function')
def log_in(driver):
    driver.get(locators.login_page_url)
    login_data = {'login': 'lizafrolova11234@mail.ru',
                  'password': '1234567'}

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.email_field)))
    driver.find_element(By.XPATH, locators.email_field).send_keys(login_data['login'])
    driver.find_element(By.XPATH, locators.password_field).send_keys(login_data['password'])
    driver.find_element(By.XPATH, locators.log_in_elements).click()

    return login_data

