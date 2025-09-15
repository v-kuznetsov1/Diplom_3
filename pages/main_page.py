import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)


    
    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_to_personal_account_button(self):
        return self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_to_order_feed_button(self):
        return self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
    

    @allure.step('Клик по кнопке "Конструктор"')
    def click_to_contructor_button(self):
        return self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
