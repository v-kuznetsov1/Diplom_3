from selenium.webdriver.common.by import By

class PersonalAccointLocators:

    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"]
    ORDER_HISTORY_BUTTON = [By.XPATH, '//a[text()="История заказов"]']
    LOGOUT_BUTTON = [By.XPATH, '//button[text()="Выход"]']

    