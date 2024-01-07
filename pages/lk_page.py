import allure
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('Переходим в личный кабинет')
    def to_lk(self, locator):
        self.click_to_element(locator)

    @allure.step('Переходим к истории заказов')
    def to_orders_history(self, locator1, locator2):
        self.click_to_element(locator1)
        self.click_to_element(locator2)

    @allure.step('Выход из аккаунта')
    def logout(self, locator1, locator2):
        self.click_to_element(locator1)
        self.click_to_element(locator2)

