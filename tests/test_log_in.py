from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.mark.parametrize('login_url', ['https://stellarburgers.nomoreparties.site/register',
                                       'https://stellarburgers.nomoreparties.site/forgot-password',
                                       'https://stellarburgers.nomoreparties.site/'])
def test_log_in_valid_values_logged_in(login_url, login_data):
    login = login_data['login']
    password = login_data['password']
    driver = webdriver.Chrome()
    driver.get(login_url)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/*[contains(text(),"Войти")]')))  # Элемент с текстом Войти
    driver.find_element(By.XPATH, './/*[contains(text(),"Войти")]').click() # Элемент с текстом Войти

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/label[text()="Email"]'))) # Поле для ввода 'Email'
    driver.find_element(By.XPATH, './/*[text() = "Email"]/parent::div/input').send_keys(login)  # Поле для ввода 'Email'
    driver.find_element(By.XPATH, './/input[@name="Пароль"]').send_keys(password)  # Поле для ввода 'Пароль'
    driver.find_element(By.XPATH, './/*[contains(text(),"Войти")]').click()  # Элемент с текстом Войти

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/p[text()="Личный Кабинет"]')))  # элемент с тектом Личный кабинет
    driver.find_element(By.XPATH, './/a[@href="/account"]').click()  # ссылка на Личный кабинет

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/*[text() = "Логин"]/parent::div/input')))  # Поле "Логин"
    login_name = driver.find_element(By.XPATH, './/*[text() = "Логин"]/parent::div/input').get_attribute(
        'value')  # Поле "Логин"
    assert login_name == login

    driver.close()


def test_log_in_personal_account_valid_values_logged_in(login_data):
    login = login_data['login']
    password = login_data['password']
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, './/a[@href="/account"]').click()  # ссылка на Личный кабинет
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/label[text()="Email"]'))) # Поле для ввода 'Email'
    driver.find_element(By.XPATH, './/*[text() = "Email"]/parent::div/input').send_keys(login)  # Поле для ввода 'Email'
    driver.find_element(By.XPATH, './/input[@name="Пароль"]').send_keys(password)  # Поле для ввода 'Пароль'
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()  # Кнопка 'Войти'
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/p[text()="Личный Кабинет"]')))  # Личный кабинет
    driver.find_element(By.XPATH, './/a[@href="/account"]').click()  # Личный кабинет

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/*[@name = "name" and @type = "text"]')))  # Поле "Логин"
    login_name = driver.find_element(By.XPATH, './/*[@name = "name" and @type = "text"]').get_attribute(
        'value')  # Поле "Логин"
    assert login_name == login

    driver.close()
