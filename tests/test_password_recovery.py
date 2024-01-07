import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, LoginPageLocators, ResetPasswordPage
from pages.password_recovery_page import PassRecoveryPage
from conftest import browser, browser_with_user, user


class TestRecoveryPass:
    def test_go_to_recovery_form(self, browser):
        PassRecoveryPage(browser).go_to_page_recover_pass(MainPageLocators.BUTT_ENTER_MAIN, LoginPageLocators.BUTT_REST_PASS)
        assert 'forgot-password' in browser.current_url

    def test_recovery_form_send_email(self, browser):
        PassRecoveryPage(browser).go_to_page_recover_pass(MainPageLocators.BUTT_ENTER_MAIN, LoginPageLocators.BUTT_REST_PASS)
        PassRecoveryPage(browser).enter_email(LoginPageLocators.EMAIL, LoginPageLocators.BUTT_REST)
        time.sleep(3)
        assert 'reset-password' in browser.current_url

    def test_recovery_form_field_pass_active(self, browser):
        PassRecoveryPage(browser).go_to_page_recover_pass(
            MainPageLocators.BUTT_ENTER_MAIN, LoginPageLocators.BUTT_REST_PASS)
        PassRecoveryPage(browser).enter_email(LoginPageLocators.EMAIL, LoginPageLocators.BUTT_REST)
        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(ResetPasswordPage.EYE))
        PassRecoveryPage(browser).click_to_element(ResetPasswordPage.EYE)
        element = PassRecoveryPage(browser).pass_field_active(ResetPasswordPage.INPUT_PASS_FOCUSED)
        assert 'text' in element

