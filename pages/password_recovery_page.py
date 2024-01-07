import allure
import string
import random
from pages.base_page import BasePage


class PassRecoveryPage(BasePage):

    @allure.step('Переходим по кнопке «Восстаносить пароль»')
    def go_to_page_recover_pass(self, locator1, locator2):
        self.click_to_element(locator1)
        self.click_to_element(locator2)

    @allure.step('Ввод почты и клик по кнопке «Восстановить»')
    def enter_email(self, locator1, locator2):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        email = f'{generate_random_string(5)}@ya.ru'
        element = self.find_element(locator1)
        element.send_keys(email)
        self.click_to_element(locator2)

    @allure.step('Проверяем, активно ли окошко ввода пароля при клике по кнопке показать/скрыть пароль')
    def pass_field_active(self, locator):
        password_input = self.find_element(locator)
        return password_input.get_attribute('type')

