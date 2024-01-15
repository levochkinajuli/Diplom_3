from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator)).click()

    def get_text(self, locator):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator)).text

    def pull(self, locator1, locator2):
        source_element = self.find_element(locator1)
        target_element = self.find_element(locator2)
        actions = ActionChains(self.driver)
        actions.click_and_hold(source_element).move_to_element(target_element).release().perform()

    def not_displayed(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element_located(locator))

    def is_displayed(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
