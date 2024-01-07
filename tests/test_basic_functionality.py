from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators
from pages.main_page import MainPage
from conftest import browser, browser_with_user, user


class TestMainPage:
    def test_click_to_constructor(self, browser):
        MainPage(browser).click_to_element(MainPageLocators.BUTT_ORDERS)
        MainPage(browser).click_to_element(MainPageLocators.BUTT_CONS)
        constructor = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(
             MainPageLocators.BUTT_CONS))
        assert constructor

    def test_click_to_orders(self, browser):
        MainPage(browser).click_to_element(MainPageLocators.BUTT_ORDERS)
        assert 'feed' in browser.current_url

    def test_get_info_of_the_element(self, browser):
        MainPage(browser).get_bun_details(MainPageLocators.BUN_FLU, MainPageLocators.DETAILS)
        element = MainPage(browser).get_text(MainPageLocators.DETAILS)
        assert 'Детали ингредиента' in element

    def test_close_details_window(self, browser):
        MainPage(browser).open_close_bun_details(MainPageLocators.BUN_FLU, MainPageLocators.CLOSE_DETAILS)
        popup_not_displayed = WebDriverWait(browser, 3).until(expected_conditions.invisibility_of_element_located(
            MainPageLocators.CLOSE_DETAILS))
        assert popup_not_displayed

    def test_counter_increase(self, browser):
        MainPage(browser).drag_buns(MainPageLocators.BUN_FLU, MainPageLocators.DRAG_BUN_FIELD)
        element = MainPage(browser).get_text(MainPageLocators.BUNS_COUNTER)
        assert '2' in element

    def test_login_user_make_order(self, browser_with_user):
        MainPage(browser_with_user).click_to_element(MainPageLocators.BUTT_ORDER)
        element = WebDriverWait(browser_with_user, 3).until(expected_conditions.visibility_of_element_located(
            MainPageLocators.ORDER_ID))
        assert 'идентификатор заказа' in element.text
