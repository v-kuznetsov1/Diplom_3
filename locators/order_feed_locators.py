
from selenium.webdriver.common.by import By


class OrderFeedLocators:

    TOTAL_ORDER = [By.XPATH, "//p[contains(@class, 'text_type_main-medium') and contains(text(), 'Выполнено за все время:')]"
    "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ') and contains(@class, 'text_type_digits-large')]"]
    
    COUNT_ORDER_TODAY = [By.XPATH, "//div//p[contains(@class, 'text_type_main-medium') and contains(text(), 'Выполнено за сегодня:')]"
    "/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ') and contains(@class, 'text_type_digits-large')]"]
    
    ORDER_IN_PROGRESS = [By.XPATH, "//li[contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2') and text()]"]
    ID_ORDER = [By.XPATH, "//p[@class='text text_type_digits-default']"]
    BUN_iN_ORDER = [By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"]
    SOUCE_IN_ORDER = [By.XPATH, "//p[text()='Соус традиционный галактический']"]
    TOPPING_IN_ORDER = [By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']"]
    CLOSE_MODAL_WINDOW_WITH_ORDER_INFO = [By.XPATH, 
                          "//section[contains(@class, 'Modal_modal_opened')]/*/button[contains(@class, "
                          "'Modal_modal__close_modified') and contains(@class, 'Modal_modal__close')]"]

