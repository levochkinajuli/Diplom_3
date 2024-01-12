import allure
from locators import LKLocators
from pages.base_page import BasePage
from urls import Urls


class PersonalAccountPage(BasePage):
    @allure.step('Переходим в личный кабинет')
    def to_lk(self):
        self.click_to_element(LKLocators.BUTT_LK)
        element = self.get_text(LKLocators.PROFILE)
        return element

    @allure.step('Переходим к истории заказов')
    def to_orders_history(self):
        self.click_to_element(LKLocators.BUTT_LK)
        element = self.get_text(LKLocators.ORDERS_HISTORY)
        return element

    @allure.step('Выходим из аккаунта')
    def logout(self):
        self.click_to_element(LKLocators.BUTT_LK)
        self.click_to_element(LKLocators.BUTT_EXIT)
        element = self.find_element(LKLocators.BUTT_ENTER_LK)
        return element.text

