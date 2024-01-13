import allure
from locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):
    @allure.step('Входим в личный кабинет')
    def login(self, email, password):
        self.driver.get(Urls.LOGIN_URL)
        self.find_element(LoginPageLocators.FIELD_EMAIL).send_keys(email)
        self.find_element(LoginPageLocators.FIELD_PASSWORD).send_keys(password)
        self.find_element(LoginPageLocators.BUTT_ENTER).click()
