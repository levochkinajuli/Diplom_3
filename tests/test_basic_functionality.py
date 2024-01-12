from pages.main_page import MainPage
from urls import Urls
from conftest import browser, browser_with_user, user


class TestMainPage:
    def test_click_to_constructor(self, browser):
        MainPage(browser).click_to_constructor()
        assert browser.current_url == Urls.MAIN_PAGE_URL

    def test_click_to_orders(self, browser):
        MainPage(browser).click_to_field_of_orders()
        assert 'feed' in browser.current_url

    def test_get_details_of_the_element(self, browser):
        assert 'Детали ингредиента' in MainPage(browser).get_bun_details().text

    def test_close_details_of_the_element(self, browser):
        assert MainPage(browser).close_bun_details()

    def test_counter_increase(self, browser):
        element = MainPage(browser).increase_counter()
        assert element == '2'

    def test_login_user_make_order(self, browser_with_user):
        element = MainPage(browser_with_user).to_order()
        assert 'идентификатор заказа' in element.text
