
from selenium.webdriver.common.by import By


class AuthorizationLocators:

    PERSONAL_ACCOUNT_BUTTON = [By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"]
    EMAIL_FIELD = [By.NAME, "name"]
    PASSWORD_FIELD = [By.NAME, 'Пароль']
    LOGIN_BUTTON = [By.XPATH, '//button[text()="Войти"]']

