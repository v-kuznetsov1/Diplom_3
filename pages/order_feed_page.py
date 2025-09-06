import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators



class OrderFeed(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    
    @allure.step('Клик по кнопке и "Лента заказов"')
    def click_order_feed_button(self):
        return self.click_to_element(OrderFeedLocators.ORDER_FEED_BUTTON)
    

    @allure.step('Получение общего количества заказов')
    def check_total_orders(self):
        return self.get_text_element(OrderFeedLocators.TOTAL_ORDER)
    
    
    @allure.step('Получение количество заказов за сегодня')
    def check_count_orders_today(self):
        return self.get_text_element(OrderFeedLocators.COUNT_ORDER_TODAY)
    
    
    @allure.step('Клик по кнопке "Конструктор"')
    def click_contructor_button(self):
        return self.click_to_element(OrderFeedLocators.CONSTRUCTOR_BUTTON)
    

    @allure.step('Получение номера заказа, находящегося в работе')
    def check_order_in_progress(self):
        return self.get_text_element(OrderFeedLocators.ORDER_IN_PROGRESS)

        
    @allure.step('Выбор в ленте созданного заказа')    
    def click_to_order(self, condition):
        return self.click_element_with_condition(OrderFeedLocators.ID_ORDER, condition)
    
    
    @allure.step('Проверка булочки в заказе')
    def check_bun_in_order(self):
        return self.find_element_by_locator(OrderFeedLocators.BUN_iN_ORDER)
    
    
    @allure.step('Проверка соуса в заказе')
    def check_souce_in_order(self):
        return self.find_element_by_locator(OrderFeedLocators.SOUCE_IN_ORDER)
    
    
    @allure.step('Проверка начинки в заказе')
    def check_topping_in_order(self):
        return self.find_element_by_locator(OrderFeedLocators.TOPPING_IN_ORDER)
    
    
    @allure.step('Закрытие модального окна с информацией о заказе')
    def close_modal_window_with_order_info(self):
        return self.click_to_element(OrderFeedLocators.CLOSE_MODAL_WINDOW_WITH_ORDER_INFO)

    
    @allure.step('Переход в личный кабинет')
    def go_to_personal_account(self):
        return self.click_to_element(OrderFeedLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step('Получение заказа из истории заказов')
    def check_order_in_orders_history(self, condition):
        return self.get_text_with_condition(OrderFeedLocators.ID_ORDER, condition)
        
            