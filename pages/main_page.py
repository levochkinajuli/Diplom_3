import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Перетаскиваем булочки для заказа')
    def drag_buns(self, locator1, locator2):
        self.pull(locator1, locator2)

    @allure.step('Нажимаем на ингредиент. Получаем подробную информацию о нем.')
    def get_bun_details(self, locator, locator1):
        self.click_to_element(locator)
        self.find_element(locator1)

    @allure.step('Нажимаем на ингредиент. Получаем подробную информацию о нем. Закрываем окно с описанием.')
    def open_close_bun_details(self, bunslocator, basketlocator):
        self.click_to_element(bunslocator)
        self.click_to_element(basketlocator)

    @allure.step('Перетаскиваем соус для заказа')
    def drag_sauce(self, saucelocator, basketlocator):
        self.pull(saucelocator, basketlocator)

    @allure.step('Перетаскиваем начинку бургера')
    def drag_filling(self, filllocator, basketlocator):
        self.pull(filllocator, basketlocator)

    @allure.step('Формируем и заказываем бургер')
    def make_order(self, bunslocator, saucelocator, filllocator, basketlocator, buttlocator, locator):
        self.drag_buns(bunslocator, basketlocator)
        self.drag_sauce(saucelocator, basketlocator)
        self.drag_filling(filllocator, basketlocator)
        self.click_to_element(buttlocator)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
