
import allure
from pages.base_page import BasePage
from locators.authorization_locators import AuthorizationLocators



class AuthorizationPage(BasePage):

    
    def __init__(self, browser):
        super().__init__(browser)


    @allure.step('Клик по кнопке "Личный кабинет"') 
    def click_personal_account_button(self):
        return self.click_to_element(AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON)
    
    
    @allure.step('Ввод email')
    def enter_email(self, email):
        return self.enter_text(AuthorizationLocators.EMAIL_FIELD, email)
    
   
    @allure.step('Ввод пароля')
    def enter_password(self, password):
        return self.enter_text(AuthorizationLocators.PASSWORD_FIELD, password)
    

    @allure.step('Клик по кнопке "Войти"')
    def click_to_login_button(self):
        return self.click_to_element(AuthorizationLocators.LOGIN_BUTTON)
    
    @allure.step('Авторизация созданного пользователя')
    def login(self, email, password):
        self.click_personal_account_button()
        self.enter_email(email)
        self.enter_password(password)
        self.click_to_login_button()

