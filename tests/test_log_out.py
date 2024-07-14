from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_log_out_from_personal_account_logged_out(log_in):
    driver = log_in

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/a[@href="/account"]')))  # ссылка на Личный кабинет
    driver.find_element(By.XPATH, './/a[@href="/account"]').click()  # ссылка на Личный кабинет

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/button[text()="Выход"]')))  # Кнопка выхода
    driver.find_element(By.XPATH, './/button[text()="Выход"]').click()  # Кнопка выхода

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/h2[text()="Вход"]')))  # Надпись 'Вход'
    assert driver.find_element(By.XPATH, './/h2[text()="Вход"]') # Надпись 'Вход'

    driver.close()
