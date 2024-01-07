from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LKLocators, MainPageLocators
from pages.lk_page import PersonalAccountPage
from conftest import browser_with_user, user


class TestPersonalAccount:
    def test_personal_account_button(self, browser_with_user):
        PersonalAccountPage(browser_with_user).to_lk(MainPageLocators.BUTT_LK)
        element = WebDriverWait(browser_with_user, 10).until(expected_conditions.visibility_of_element_located(
            LKLocators.PROFILE))
        assert 'Профиль' in element.text

    def test_orders_history_button(self, browser_with_user):
        PersonalAccountPage(browser_with_user).to_orders_history(MainPageLocators.BUTT_LK, LKLocators.ORDERS_HISTORY)
        assert 'order-history' in browser_with_user.current_url

    def test_logout(self, browser_with_user):
        PersonalAccountPage(browser_with_user).logout(MainPageLocators.BUTT_LK, LKLocators.BUTT_EXIT)
        element = WebDriverWait(browser_with_user, 3).until(expected_conditions.visibility_of_element_located(LKLocators.BUTT_ENTER_LK))
        assert 'Войти' in element.text
