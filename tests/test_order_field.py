import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, OrdersFieldLocators
from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from conftest import browser, browser_with_user, user


class TestOrderFieldPage:
    def test_open_details_of_the_order(self, browser):
        MainPage(browser).click_to_element(MainPageLocators.BUTT_ORDERS)
        OrdersPage(browser).push_to_order(OrdersFieldLocators.ORDER)
        element = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(
            OrdersFieldLocators.COMPOUND))
        assert "Cостав" in element.text

    def test_find_users_orders_in_all_orders(self, browser_with_user):
        MainPage(browser_with_user).make_order(
            MainPageLocators.BUN_FLU, MainPageLocators.SAU_SPICY, MainPageLocators.FILL_METEOR, MainPageLocators.BASKET, MainPageLocators.BUTT_ORDER, OrdersFieldLocators.WAIT)
        element = OrdersPage(browser_with_user).get_orders_number(OrdersFieldLocators.ORDERS_ID_IN_ORDER)
        MainPage(browser_with_user).click_to_element(OrdersFieldLocators.TO_CLOSE_ORDER)
        MainPage(browser_with_user).click_to_element(MainPageLocators.BUTT_ORDERS)
        time.sleep(2)
        element2 = WebDriverWait(browser_with_user, 3).until(expected_conditions.visibility_of_element_located(
            OrdersFieldLocators.ORDER_NUM))
        assert element in element2.text

    def test_total_summ_of_orders(self, browser_with_user):
        MainPage(browser_with_user).click_to_element(MainPageLocators.BUTT_ORDERS)
        element = OrdersPage(browser_with_user).get_all_orders_number(OrdersFieldLocators.ALL_ORDERS)
        MainPage(browser_with_user).click_to_element(MainPageLocators.BUTT_CONS)
        MainPage(browser_with_user).make_order(
            MainPageLocators.BUN_FLU, MainPageLocators.SAU_SPICY, MainPageLocators.FILL_METEOR, MainPageLocators.BASKET,
            MainPageLocators.BUTT_ORDER, OrdersFieldLocators.WAIT)
        MainPage(browser_with_user).click_to_element(OrdersFieldLocators.TO_CLOSE_ORDER)
        MainPage(browser_with_user).click_to_element(MainPageLocators.BUTT_ORDERS)
        element2 = OrdersPage(browser_with_user).get_all_orders_number(OrdersFieldLocators.ALL_ORDERS)
        assert element != element2

    def test_today_summ_of_orders(self, browser_with_user):
        MainPage(browser_with_user).click_to_element(MainPageLocators.BUTT_ORDERS)
        element = OrdersPage(browser_with_user).get_today_orders_number(OrdersFieldLocators.TODAY_ORDERS)
        MainPage(browser_with_user).click_to_element(MainPageLocators.BUTT_CONS)
        MainPage(browser_with_user).make_order(
            MainPageLocators.BUN_FLU, MainPageLocators.SAU_SPICY, MainPageLocators.FILL_METEOR, MainPageLocators.BASKET,
            MainPageLocators.BUTT_ORDER, OrdersFieldLocators.WAIT)
        MainPage(browser_with_user).click_to_element(OrdersFieldLocators.TO_CLOSE_ORDER)
        MainPage(browser_with_user).click_to_element(MainPageLocators.BUTT_ORDERS)
        element2 = OrdersPage(browser_with_user).get_today_orders_number(OrdersFieldLocators.TODAY_ORDERS)
        assert element != element2

    def test_find_order_in_work(self, browser_with_user):
        MainPage(browser_with_user).make_order(
            MainPageLocators.BUN_FLU, MainPageLocators.SAU_SPICY, MainPageLocators.FILL_METEOR, MainPageLocators.BASKET, MainPageLocators.BUTT_ORDER, OrdersFieldLocators.WAIT)
        element = OrdersPage(browser_with_user).get_orders_number(OrdersFieldLocators.ORDERS_ID_IN_ORDER)
        MainPage(browser_with_user).click_to_element(OrdersFieldLocators.TO_CLOSE_ORDER)
        MainPage(browser_with_user).click_to_element(MainPageLocators.BUTT_ORDERS)
        element2 = WebDriverWait(browser_with_user, 3).until(expected_conditions.visibility_of_element_located(
            OrdersFieldLocators.ORDER_IN_WORK))
        assert element in element2.text
