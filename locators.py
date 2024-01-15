from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTT_CONS = By.XPATH, ".//p[text() = 'Конструктор']"
    BUTT_ORDERS = By.XPATH, ".//p[text() = 'Лента Заказов']"
    BUTT_ENTER_MAIN = By.XPATH, ".//button[text() = 'Войти в аккаунт']"
    BUN_FLU = By.XPATH, ".//p[text() = 'Флюоресцентная булка R2-D3']"
    DETAILS = By.XPATH, "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']"
    CLOSE_DETAILS = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]"
    DRAG_BUN_FIELD = By.XPATH, ".//span[contains(text(), 'Перетяните булочку сюда (верх)')]"
    BUNS_COUNTER = By.XPATH, "//p[@class='counter_counter__num__3nue1']"
    BUTT_TO_ORDER = By.XPATH, ".//button[text() = 'Оформить заказ']"
    ORDER_ID_NUM = By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"
    ORDER_ID = By.XPATH, "//p[@class='undefined text text_type_main-medium mb-15']"
    BASKET = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]//li[contains(@class, 'BurgerConstructor_basket__listItem__aWMu1')]"
    FILL_METEOR = By.XPATH, ".//p[text() = 'Говяжий метеорит (отбивная)']"
    SAU_SPICY = By.XPATH, ".//p[text() = 'Соус Spicy-X']"
    TO_CLOSE_ORDER = By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    BUNS_FLO_PRICE = By.XPATH, "//p[@class='text text_type_digits-medium mr-3' and text()='1976']"
    ORDER_ID_NUM_NOT_VALID = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'Modal_modal__title__2L34m') and contains(@class, 'text') and contains(@class, 'text_type_digits-large') and contains(@class, 'mb-8') and text()='9999']"


class LoginPageLocators:
    FIELD_EMAIL = By.NAME, "name"
    FIELD_PASSWORD = By.NAME, "Пароль"
    BUTT_ENTER = By.XPATH, ".//button[text() = 'Войти']"
    BUTT_ALR_REG = By.XPATH, ".//a[@href='/login']"
    BUTT_LOGOUT = By.XPATH, ".//button[text() = 'Выход']"


class LKLocators:
    BUTT_LK = By.LINK_TEXT, "Личный Кабинет"
    PROFILE = By.XPATH, "//a[text()='Профиль']"
    ORDERS_HISTORY = By.XPATH, "//a[text()='История заказов']"
    BUTT_EXIT = By.XPATH, ".//button[text() = 'Выход']"
    BUTT_ENTER_LK = By.XPATH, ".//button[text() = 'Войти']"


class OrdersFieldLocators:
    ORDER = By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']"
    COMPOUND = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"
    ORDERS_ID_IN_ORDER = By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"
    ORDER_NUM = By.XPATH, "//p[@class='text text_type_digits-default']"
    ALL_ORDERS = By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    TODAY_ORDERS = By.XPATH, "//p[text()='Выполнено за сегодня:']/parent::*"
    ORDER_IN_WORK = By.XPATH, "//li[@class='text text_type_digits-default mb-2']"


class ResetPasswordLocators:
    EYE = By.XPATH, "//div[@class='input__icon input__icon-action']"
    INPUT_PASS_FOCUSED = By.XPATH, "//div[contains(@class, 'input_status_active')]"
    BUTT_REST_PASS = By.XPATH, ".//a[text() = 'Восстановить пароль']"
    EMAIL = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default']//label[contains(text(), 'Email')]/following-sibling::input"
    BUTT_REST = By.XPATH, ".//button[text() = 'Восстановить']"
    FIELD_PASS_REST = By.XPATH, "//h2[text()='Восстановление пароля']"
