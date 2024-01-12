import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    @allure.step('Проверяем кнопку "Конструктор"')
    def click_to_constructor(self):
        self.driver.get(Urls.MAIN_PAGE_URL)
        self.click_to_element(MainPageLocators.BUTT_ORDERS)
        self.click_to_element(MainPageLocators.BUTT_CONS)

    @allure.step('Проверяем кнопку "Лента заказов"')
    def click_to_field_of_orders(self):
        self.driver.get(Urls.MAIN_PAGE_URL)
        self.click_to_element(MainPageLocators.BUTT_ORDERS)

    @allure.step('Нажимаем на ингредиент. Получаем подробную информацию о нем.')
    def get_bun_details(self):
        self.driver.get(Urls.MAIN_PAGE_URL)
        self.click_to_element(MainPageLocators.BUN_FLU)
        element = self.find_element(MainPageLocators.DETAILS)
        return element

    @allure.step('Нажимаем на ингредиент. Получаем подробную информацию о нем. Закрываем окно с описанием.')
    def close_bun_details(self):
        self.driver.get(Urls.MAIN_PAGE_URL)
        self.click_to_element(MainPageLocators.BUN_FLU)
        self.find_element(MainPageLocators.DETAILS)
        self.click_to_element(MainPageLocators.CLOSE_DETAILS)
        return self.not_displayed(MainPageLocators.CLOSE_DETAILS)

    @allure.step('Перетаскиваем булочки для заказа')
    def drag_buns(self):
        self.pull(MainPageLocators.BUN_FLU, MainPageLocators.DRAG_BUN_FIELD)

    @allure.step('Проверяем счетчик ингредиентов')
    def increase_counter(self):
        self.driver.get(Urls.MAIN_PAGE_URL)
        self.pull(MainPageLocators.BUN_FLU, MainPageLocators.DRAG_BUN_FIELD)
        return self.get_text(MainPageLocators.BUNS_COUNTER)

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def to_order(self):
        self.click_to_element(MainPageLocators.BUTT_TO_ORDER)
        return self.find_element(MainPageLocators.ORDER_ID)

    @allure.step('Перетаскиваем соус для заказа')
    def drag_sauce(self):
        self.pull(MainPageLocators.SAU_SPICY, MainPageLocators.BASKET)

    @allure.step('Перетаскиваем начинку бургера')
    def drag_filling(self):
        self.pull(MainPageLocators.FILL_METEOR, MainPageLocators.BASKET)

    @allure.step('Формируем и заказываем бургер')
    def make_order(self):
        self.drag_buns()
        self.drag_sauce()
        self.drag_filling()
        self.to_order()

    @allure.step('Получаем номер заказа')
    def get_valid_order_number(self):
        self.not_displayed(MainPageLocators.ORDER_ID_NUM_NOT_VALID)
        element = self.find_element(MainPageLocators.ORDER_ID_NUM)
        return element.text

    @allure.step('Закрываем окно заказа')
    def to_close_order(self):
        return self.click_to_element(MainPageLocators.TO_CLOSE_ORDER)

    @allure.step('Оформляем заказ и получаем его номер')
    def make_order_and_get_order_number(self):
        self.make_order()
        element = self.get_valid_order_number()
        self.to_close_order()
        return element

    @allure.step('Оформляем заказ и закрываем его')
    def make_order_and_close(self):
        self.driver.get(Urls.MAIN_PAGE_URL)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BUTT_CONS))
        self.make_order()
        self.to_close_order()
