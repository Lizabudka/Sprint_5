from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_click_on_section_sauce_jumping_to_section_sauce():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')  # Страница входа

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/span[text()="Соусы"]')))  # Секция с соусами

    driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()  # Секция с соусами
    section_class = driver.find_element(
        By.XPATH, './/span[text()="Соусы"]/parent::div').get_attribute('class')  # Секция с соусами
    assert 'current' in section_class

    driver.close()


def test_click_on_section_bun_jumping_to_section_bun():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')  # Страница входа

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/span[text()="Булки"]')))  # Секция с булками

    driver.find_element(By.XPATH, './/span[text()="Начинки"]').click()  # Секция с начинками
    driver.find_element(By.XPATH, './/span[text()="Булки"]').click()  # Секция с булками
    section_class = driver.find_element(
        By.XPATH, './/span[text()="Булки"]/parent::div').get_attribute('class')  # Секция с булками
    assert 'current' in section_class

    driver.close()


def test_click_on_section_filling_jumping_to_section_filling():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')  # Страница входа

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((
            By.XPATH, './/span[text()="Соусы"]')))  # Секция с соусами

    driver.find_element(By.XPATH, './/span[text()="Начинки"]').click()  # Секция с начинками
    section_class = driver.find_element(
        By.XPATH, './/span[text()="Начинки"]/parent::div').get_attribute('class')  # Секция с начинками
    assert 'current' in section_class

    driver.close()
