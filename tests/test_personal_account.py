import allure

from pages.lk_page import PersonalAccountPage
from conftest import browser_with_user, browser, user


class TestPersonalAccount:
    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_personal_account_button(self, browser_with_user):
        assert 'Профиль' in PersonalAccountPage(browser_with_user).to_lk()

    @allure.title("Проверка перехода в раздел «История заказов»")
    def test_orders_history_button(self, browser_with_user):
        assert 'История заказов' in PersonalAccountPage(browser_with_user).to_orders_history()

    @allure.title("Проверка выхода из личного кабинета")
    def test_logout(self, browser_with_user):
        assert 'Войти' in PersonalAccountPage(browser_with_user).logout()
