import allure
from locators import OrdersFieldLocators
from pages.base_page import BasePage
from urls import Urls


class OrdersPage(BasePage):
    @allure.step('Открываем всплывающее окно с деталями заказа')
    def push_to_order(self):
        self.driver.get(Urls.ORDER_FIELD_URL)
        self.is_displayed(OrdersFieldLocators.ORDER)
        self.click_to_element(OrdersFieldLocators.ORDER)
        return self.find_element(OrdersFieldLocators.COMPOUND)

    @allure.step('Получаем номер последнего заказа в списке всех заказов')
    def get_last_order_number_in_list(self):
        self.driver.get(Urls.ORDER_FIELD_URL)
        element = self.find_element(OrdersFieldLocators.ORDER_NUM)
        return element.text

    @allure.step('Получаем oбщее количество всех заказов')
    def get_all_orders_number(self):
        self.driver.get(Urls.ORDER_FIELD_URL)
        self.is_displayed(OrdersFieldLocators.ALL_ORDERS)
        element = self.get_text(OrdersFieldLocators.ALL_ORDERS)
        return element

    @allure.step('Получаем количество всех заказов на сегодня')
    def get_today_orders_number(self):
        self.driver.get(Urls.ORDER_FIELD_URL)
        self.is_displayed(OrdersFieldLocators.TODAY_ORDERS)
        element = self.get_text(OrdersFieldLocators.TODAY_ORDERS)
        return element

    @allure.step('Находим заказ в разделе "В работе"')
    def get_order_in_work(self):
        self.driver.get(Urls.ORDER_FIELD_URL)
        element = self.is_displayed(OrdersFieldLocators.ORDER_IN_WORK)
        return element
