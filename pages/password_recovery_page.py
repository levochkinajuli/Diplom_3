import allure
from locators import ResetPasswordLocators
from pages.base_page import BasePage
from urls import Urls


class PassRecoveryPage(BasePage):

    @allure.step('Переходим по кнопке «Восстаносить пароль»')
    def go_to_page_recover_pass(self):
        self.driver.get(Urls.LOGIN_URL)
        self.click_to_element(ResetPasswordLocators.BUTT_REST_PASS)

    @allure.step('Ввод почты и клик по кнопке «Восстановить»')
    def enter_email(self):
        self.go_to_page_recover_pass()
        element = self.find_element(ResetPasswordLocators.EMAIL)
        element.send_keys('12345jjll@ya.ru')
        self.click_to_element(ResetPasswordLocators.BUTT_REST)
        return self.get_text(ResetPasswordLocators.FIELD_PASS_REST)

    @allure.step('Проверяем, активно ли окошко ввода пароля при клике по кнопке показать/скрыть пароль')
    def pass_field_active(self):
        self.go_to_page_recover_pass()
        element = self.find_element(ResetPasswordLocators.EMAIL)
        element.send_keys('12345jjll@ya.ru')
        self.click_to_element(ResetPasswordLocators.BUTT_REST)
        self.click_to_element(ResetPasswordLocators.EYE)
        return self.find_element(ResetPasswordLocators.INPUT_PASS_FOCUSED)
