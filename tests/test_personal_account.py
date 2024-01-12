from pages.lk_page import PersonalAccountPage
from conftest import browser_with_user, user


class TestPersonalAccount:
    def test_personal_account_button(self, browser_with_user):
        assert 'Профиль' in PersonalAccountPage(browser_with_user).to_lk()

    def test_orders_history_button(self, browser_with_user):
        assert 'История заказов' in PersonalAccountPage(browser_with_user).to_orders_history()

    def test_logout(self, browser_with_user):
        assert 'Войти' in PersonalAccountPage(browser_with_user).logout()
