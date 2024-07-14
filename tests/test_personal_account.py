from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_click_on_personal_account_when_logged_in_transmit_to_personal_account(log_in):
    driver = log_in

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/a[@href="/account"]')))  # ссылка в Личный кабинет
    driver.find_element(By.XPATH, './/a[@href="/account"]').click()  # ссылка в Личный кабинет

    WebDriverWait(driver, 5).until(expected_conditions.url_contains('profile'))
    account_url = 'https://stellarburgers.nomoreparties.site/account/profile'  # ссылка в Личный кабинет
    assert driver.current_url == account_url

    driver.close()


def test_click_on_personal_account_when_not_logged_transmit_to_login_page(log_in):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/a[@href="/account"]')))  # ссылка в Личный кабинет
    driver.find_element(By.XPATH, './/a[@href="/account"]').click()  # Личный кабинет

    WebDriverWait(driver, 5).until(expected_conditions.url_contains('login'))
    account_url = 'https://stellarburgers.nomoreparties.site/login'  # ссылка на вход
    assert driver.current_url == account_url

    driver.close()
