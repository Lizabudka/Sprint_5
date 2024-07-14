from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_valid_data_registration_complited(registration, random_login, random_password):
    driver = registration
    password = random_password
    login = random_login

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/a[text()="Зарегистрироваться"]')))  # Ссылка 'Зарегестрироваться'
    driver.find_element(By.XPATH, './/a[text()="Зарегистрироваться"]').click()  # Ссылка 'Зарегестрироваться'

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/*[text() = "Имя"]/parent::div/input')))  # Поле ввода 'Имя'
    driver.find_element(By.XPATH, './/*[text() = "Имя"]/parent::div/input').send_keys('Test')  # Поле ввода 'Имя'
    driver.find_element(By.XPATH, './/*[text() = "Email"]/parent::div/input').send_keys(login)  # Поле ввода 'Email'
    driver.find_element(By.XPATH, './/input[@name="Пароль"]').send_keys(password)  # Поле ввода 'Пароль'
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()  # Кнопка 'Зарегистрироваться'

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/p[text()="Такой пользователь уже существует"]')))  # надпись после попвтки повторной регистрации
    assert driver.find_element(By.XPATH, './/p[text()="Такой пользователь уже существует"]').text

    driver.close()


def test_registration_4_digit_password_incorrect_password_error(random_login):
    random_login = random_login
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(By.XPATH, './/a[@href="/account"]').click()  # Личный кабинет

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/*[text()="Зарегистрироваться"]')))  # Ссылка 'Зарегестрироваться'
    driver.find_element(By.XPATH, './/*[@href="/register"]').click()  # Ссылка 'Зарегестрироваться'

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/*[text() = "Имя"]/parent::div/input')))  # Поле ввода 'Имя'
    driver.find_element(
        By.XPATH, './/*[text() = "Имя"]/parent::div/input').send_keys('Лиза')  # Поле ввода 'Имя'
    driver.find_element(
        By.XPATH, './/*[text() = "Email"]/parent::div/input').send_keys(random_login)  # Поле ввода 'Email'
    driver.find_element(By.XPATH, './/input[@type="password"]').send_keys('1234')  # Поле ввода 'Пароль'
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()  # Кнопка 'Зарегистрироваться'

    assert 'Некорректный пароль' == driver.find_element(
        By.XPATH, './/p[text()="Некорректный пароль"]').text  # ошибка о нееорректном пароле

    driver.close()
