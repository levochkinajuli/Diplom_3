import time
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class OrdersPage(BasePage):

    @allure.step('Нажимаем на кнопку "Оформить заказ')
    def push_to_order(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))
        self.click_to_element(locator)

    @allure.step('Получаем номер заказа')
    def get_orders_number(self, locator):
        time.sleep(2)
        element = self.get_text(locator)
        return element

    @allure.step('Получаем oбщее количество всех заказов')
    def get_all_orders_number(self, locator):
        WebDriverWait(self.driver, 3)
        element = self.get_text(locator)
        return element

    @allure.step('Получаем количество всех заказов на сегодня')
    def get_today_orders_number(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))
        element = self.get_text(locator)
        return element
