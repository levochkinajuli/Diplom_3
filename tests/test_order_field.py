import allure
from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from conftest import browser, browser_with_user, user


class TestOrderFieldPage:
    @allure.title("Проверка появления окна с содержанием заказа при клике на заказ")
    def test_open_details_of_the_order(self, browser):
        assert "Cостав" in OrdersPage(browser).push_to_order().text

    @allure.title("Проверка отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов»")
    def test_find_order_in_all_orders(self, browser_with_user):
        element = MainPage(browser_with_user).make_order_and_get_order_number()
        element2 = OrdersPage(browser_with_user).get_last_order_number_in_list()
        assert element in element2

    @allure.title("Проверка счётчика 'Выполнено за всё время' при создании нового заказа")
    def test_increase_total_summ_of_orders_after_order(self, browser_with_user):
        element = OrdersPage(browser_with_user).get_all_orders_number()
        MainPage(browser_with_user).make_order_and_close()
        element2 = OrdersPage(browser_with_user).get_all_orders_number()
        assert element != element2

    @allure.title("Проверка счётчика 'Выполнено за сегодня' при создании нового заказа")
    def test_today_summ_of_orders(self, browser_with_user):
        element = OrdersPage(browser_with_user).get_today_orders_number()
        MainPage(browser_with_user).make_order_and_close()
        element2 = OrdersPage(browser_with_user).get_today_orders_number()
        assert element != element2

    @allure.title("Проверка номера нового заказа в разделе В работе")
    def test_find_order_in_work(self, browser_with_user):
        element = MainPage(browser_with_user).make_order_and_get_order_number()
        element2 = OrdersPage(browser_with_user).get_order_in_work()
        assert element in element2.text
