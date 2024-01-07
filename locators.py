from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTT_ENTER_MAIN = By.XPATH, ".//button[text() = 'Войти в аккаунт']"
    BUTT_LK = By.LINK_TEXT, "Личный Кабинет"
    BUTT_ORDER = By.XPATH, ".//button[text() = 'Оформить заказ']"
    BUTT_CONS = By.XPATH, ".//p[text() = 'Конструктор']"
    FILL_METEOR = By.XPATH, ".//p[text() = 'Говяжий метеорит (отбивная)']"
    SAU_SPICY = By.XPATH, ".//p[text() = 'Соус Spicy-X']"
    BUN_FLU = By.XPATH, ".//p[text() = 'Флюоресцентная булка R2-D3']"
    DRAG_BUN_FIELD = By.XPATH, ".//span[contains(text(), 'Перетяните булочку сюда (верх)')]"
    BUNS_FLO_PRICE = By.XPATH, "//p[@class='text text_type_digits-medium mr-3' and text()='1976']"
    BUNS_COUNTER = By.XPATH, "//p[@class='counter_counter__num__3nue1']"
    DETAILS = By.XPATH, "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']"
    CLOSE_DETAILS = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]"
    BUTT_ORDERS = By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Лента Заказов']"
    ORDER_ID = By.XPATH, "//p[@class='undefined text text_type_main-medium mb-15']"
    BASKET = By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]//li[contains(@class, 'BurgerConstructor_basket__listItem__aWMu1')]"


class LoginPageLocators:
    FIELD_EMAIL = By.NAME, "name"
    FIELD_PASSWORD = By.NAME, "Пароль"
    BUTT_ENTER = By.XPATH, ".//button[text() = 'Войти']"
    BUTT_REST_PASS = By.XPATH, ".//a[text() = 'Восстановить пароль']"
    BUTT_ALR_REG = By.XPATH, ".//a[@href='/login']"
    BUTT_LOGOUT = By.XPATH, ".//button[text() = 'Выход']"
    BUTT_REST = By.XPATH, ".//button[text() = 'Восстановить']"
    EMAIL = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default']//label[contains(text(), 'Email')]/following-sibling::input"


class LKLocators:
    PROFILE = By.XPATH, "//a[text()='Профиль']"
    ORDERS_HISTORY = By.XPATH, "//a[text()='История заказов']"
    BUTT_EXIT = By.XPATH, ".//button[text() = 'Выход']"
    BUTT_ENTER_LK = By.XPATH, ".//button[text() = 'Войти']"


class OrdersFieldLocators:
    ORDER = By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']"
    ORDER_FEED_TITLE = By.CLASS_NAME, "text_type_main-large"
    COMPOUND = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"
    ORDERS_ID_IN_ORDER = By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"
    TO_CLOSE_ORDER = By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    ORDER_NUM = By.XPATH, "//p[@class='text text_type_digits-default']"
    WAIT = By.XPATH, "//p[contains(@class, 'text_type_main-default') and contains(@class, 'text_color_inactive') and contains(text(), 'Дождитесь готовности на орбитальной станции')]"
    ALL_ORDERS = By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    TODAY_ORDERS = By.XPATH, "//p[text()='Выполнено за сегодня:']/parent::*"
    ORDER_IN_WORK = By.XPATH, "//li[@class='text text_type_digits-default mb-2']"


class ResetPasswordPage:
    EYE = By.XPATH, "//div[@class='input__icon input__icon-action']"
    INPUT_PASS_FOCUSED = By.XPATH, "//label[text()='Пароль']/following-sibling::input"
