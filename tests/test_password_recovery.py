from pages.password_recovery_page import PassRecoveryPage
from conftest import browser, browser_with_user, user


class TestRecoveryPass:
    def test_go_to_recovery_form(self, browser):
        PassRecoveryPage(browser).go_to_page_recover_pass()
        assert 'forgot-password' in browser.current_url

    def test_recovery_form_send_email(self, browser):
        assert 'Восстановление пароля' in PassRecoveryPage(browser).enter_email()

    def test_recovery_form_field_pass_active(self, browser):
        assert PassRecoveryPage(browser).pass_field_active()
