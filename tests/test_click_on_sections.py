from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


def test_click_on_section_sauce_jumping_to_section_sauce(driver):
    driver.get(locators.home_page_url)

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.souce_section_name)))

    driver.find_element(By.XPATH, locators.souce_section_name).click()
    section_class = driver.find_element(By.XPATH, locators.souce_section).get_attribute('class')
    assert 'current' in section_class


def test_click_on_section_bun_jumping_to_section_bun(driver):
    driver.get(locators.home_page_url)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.buns_section_name)))

    driver.find_element(By.XPATH, locators.filling_section_name).click()
    driver.find_element(By.XPATH, locators.buns_section_name).click()
    section_class = driver.find_element(By.XPATH, locators.buns_section).get_attribute('class')
    assert 'current' in section_class


def test_click_on_section_filling_jumping_to_section_filling(driver):
    driver.get(locators.home_page_url)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.souce_section)))

    driver.find_element(By.XPATH, locators.filling_section_name).click()
    section_class = driver.find_element(By.XPATH, locators.filling_section).get_attribute('class')
    assert 'current' in section_class
