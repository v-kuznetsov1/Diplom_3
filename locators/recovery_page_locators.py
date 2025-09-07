
from selenium.webdriver.common.by import By

class RecoveryPasswordLocators:

    RECOVERY_PASSWORD_BUTTUN = [By.XPATH, '//a[contains(text(), "Восстановить пароль")]']
    EMAIL_FIELD = [By.CSS_SELECTOR, 'input.text']
    RECOVERY_BUTTON = [By.XPATH, '//button[contains(text(), "Восстановить")]']
    SHOW_HIDE_BUTTON = [By.CSS_SELECTOR, '.input__icon']
    PASSWORD_FIELD = [By.CSS_SELECTOR, 'div.input_status_active']
    