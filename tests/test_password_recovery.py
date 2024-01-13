import allure
from pages.password_recovery_page import PassRecoveryPage
from conftest import browser, browser_with_user, user


class TestRecoveryPass:
    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_recovery_form(self, browser):
        PassRecoveryPage(browser).go_to_page_recover_pass()
        assert 'forgot-password' in browser.current_url

    @allure.title("Проверка ввода почты и клик по кнопке «Восстановить»")
    def test_recovery_form_send_email(self, browser):
        assert 'Восстановление пароля' in PassRecoveryPage(browser).enter_email()

    @allure.title("Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_recovery_form_field_pass_active(self, browser):
        assert PassRecoveryPage(browser).pass_field_active()
