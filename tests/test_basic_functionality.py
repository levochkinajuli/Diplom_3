import allure
from pages.main_page import MainPage
from urls import Urls
from conftest import browser, browser_with_user, user


class TestMainPage:
    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_click_to_constructor(self, browser):
        MainPage(browser).click_to_constructor()
        assert browser.current_url == Urls.MAIN_PAGE_URL

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_click_to_orders(self, browser):
        MainPage(browser).click_to_field_of_orders()
        assert 'feed' in browser.current_url

    @allure.title("Проверка клика на ингредиент, появляется окно с деталями")
    def test_get_details_of_the_element(self, browser):
        assert 'Детали ингредиента' in MainPage(browser).get_bun_details().text

    @allure.title("Проверка окно с деталями закрывается кликом по крестику")
    def test_close_details_of_the_element(self, browser):
        assert MainPage(browser).close_bun_details()

    @allure.title("Проверка при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_counter_increase(self, browser):
        element = MainPage(browser).increase_counter()
        assert element == '2'

    @allure.title("Проверка возможности оформления заказа залогиненным пользователем")
    def test_login_user_make_order(self, browser_with_user):
        element = MainPage(browser_with_user).to_order()
        assert 'идентификатор заказа' in element.text
