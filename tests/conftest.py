from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import random
import string


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
def login_data():
    login_data = {'login': 'lizafrolova11234@mail.ru',
                  'password': '1234567'}
    return login_data


@pytest.fixture(scope='function')
def registration(random_login, random_password):
    login = random_login
    password = random_password

    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((
        By.XPATH, './/*[text() = "Имя"]/parent::div/input')))  # Поле ввода 'Имя'
    driver.find_element(By.XPATH, './/*[text() = "Имя"]/parent::div/input').send_keys('Test')  # Поле ввода 'Имя'
    driver.find_element(By.XPATH, './/*[text() = "Email"]/parent::div/input').send_keys(login)  # Поле ввода 'Email'
    driver.find_element(By.XPATH, './/input[@type="password"]').send_keys(password)  # Поле ввода 'Пароль'
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()  # Кнопка 'Зарегистрироваться'

    return driver


@pytest.fixture(scope='function')
def log_in(login_data):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/*[text() = "Email"]/parent::div/input')))  # Поле ввода Email
    driver.find_element(
        By.XPATH, './/*[text() = "Email"]/parent::div/input').send_keys(login_data['login'])  # Поле ввода Email
    driver.find_element(By.XPATH, './/input[@name="Пароль"]').send_keys(login_data['password'])  # Поле ввода Пароль
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()  # кнопка "Войти"

    return driver
