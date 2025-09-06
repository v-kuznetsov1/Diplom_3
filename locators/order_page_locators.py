
from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_FEED_BUTTON = [By.XPATH, '//p[text()="Лента Заказов"]']
    CONSTRUCTOR_BUTTON = [By.XPATH, '//p[text()="Конструктор"]']
    BUN = [By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"]
    MODAL_WINDOW = [By.CLASS_NAME, "Modal_modal__container__Wo2l_"]
    CLOSE_MODAL_WINDOW = [By.XPATH, 
                          "//section[contains(@class, 'Modal_modal_opened')]/*/button[contains(@class, "
                          "'Modal_modal__close_modified') and contains(@class, 'Modal_modal__close')]"]
    
    CONSTRUCTOR_BURGER = [By.CLASS_NAME, 'constructor-element__row']

    COUNTER_INGREDIENT = [By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]//p[contains(@class, 'counter_counter__num__3nue1')]"]

    SAUCES_BUTTON = [By.XPATH, '//span[text()="Соусы"]']
    SAUCE = [By.XPATH, "//img[@alt='Соус Spicy-X']"]

    TOPPINGS_BUTTON = [By.XPATH, '//span[text()="Начинки"]']
    TOPPING = [By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']"]

    CREATE_ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]
    MODAL_WINDOW_WITH_ORDER_INFO = [By.CLASS_NAME, 'Modal_modal__contentBox__sCy8X']
    ORDER_ID = [By.CLASS_NAME, 'Modal_modal__title_shadow__3ikwq']
    STATUS_ORDER = [By.XPATH, "//p[contains(@class, 'undefined') and text()='Ваш заказ начали готовить']"]

    CLOSE_MODAL_WINDOW_WITH_ORDER_INFO = [By.CSS_SELECTOR, 'button.Modal_modal__close__TnseK']

