
import allure
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccointLocators


class PersonalAccountPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Переход в личный кабинет')
    def go_to_personal_account(self):
        return self.click_to_element(PersonalAccointLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Переход на страницу истории заказов')
    def click_to_order_history(self):
        return self.click_to_element(PersonalAccointLocators.ORDER_HISTORY_BUTTON)
    
    @allure.step('Выход из аккаунта пользователя')
    def click_to_logout_button(self):
        return self.click_to_element(PersonalAccointLocators.LOGOUT_BUTTON)
    
    @allure.step("Проверка ожидаемого url'a")
    def get_expected_url(self, url):
        return self.check_current_url(url)
    
