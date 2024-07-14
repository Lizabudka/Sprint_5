from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_click_on_constructor_from_personal_account_transition_to_main_page(log_in):
    driver = log_in

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, './/a[@href="/account"]')))  # ссылка в Личный кабинет
    driver.find_element(By.XPATH, './/a[@href="/account"]').click()  # ссылка в Личный кабинет

    WebDriverWait(driver, 5).until((expected_conditions.visibility_of_element_located(
        (By.XPATH, './/div[contains(@class, "logo")]/a'))))  # Логотип
    driver.find_element(By.XPATH, './/div[contains(@class, "logo")]/a').click()  # Логотип

    account_url = 'https://stellarburgers.nomoreparties.site/'  # главная страница с конструктором
    assert driver.current_url == account_url

    driver.close()


def test_click_on_logo_from_personal_account_transition_to_main_page(log_in):
    driver = log_in

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, './/a[@href="/account"]')))  # ссылка в Личный кабинет
    driver.find_element(By.XPATH, './/a[@href="/account"]').click()  # ссылка в Личный кабинет

    WebDriverWait(driver, 5).until((expected_conditions.visibility_of_element_located(
        (By.XPATH, './/p[text()="Конструктор"]/parent::a'))))  # Ссылка на главную страницус Конструктором
    driver.find_element(By.XPATH, './/p[text()="Конструктор"]/parent::a').click()
    # Ссылка на главную страницус Конструктором

    account_url = 'https://stellarburgers.nomoreparties.site/'  # главная страница с конструктором
    assert driver.current_url == account_url

    driver.close()
