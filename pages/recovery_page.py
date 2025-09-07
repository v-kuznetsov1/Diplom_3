
import allure
from pages.base_page import BasePage
from locators.recovery_page_locators import RecoveryPasswordLocators
from data import TestData


class RecoveryPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    
    
    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_to_recovery_password_button(self):
        return self.click_to_element(RecoveryPasswordLocators.RECOVERY_PASSWORD_BUTTUN)
    
    
    @allure.step("Ввода email'a")
    def enter_email(self):
        return self.enter_text(RecoveryPasswordLocators.EMAIL_FIELD, TestData.test_email)
    

    @allure.step('Кликл по кнопке "Восстановить')
    def click_to_recovery_button(self):
        return self.click_to_element(RecoveryPasswordLocators.RECOVERY_BUTTON)
    

    @allure.step("Клик по кнопке, делающей пароль видимым")
    def click_to_hide_button(self):
        return self.click_to_element(RecoveryPasswordLocators.SHOW_HIDE_BUTTON)
    
    
    @allure.step('Проверка, что кнопка, делающая пароль видимым, работает корректно')
    def get_show_password(self):
        return self.get_attribute_element(RecoveryPasswordLocators.PASSWORD_FIELD, 'class')

