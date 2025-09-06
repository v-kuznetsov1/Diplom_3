
import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_order_feed_button(self):
        return self.click_to_element(OrderPageLocators.ORDER_FEED_BUTTON)
    
    
    @allure.step("Проверка ожидаемого url'a")
    def check_current_url(self, url):
        return super().check_current_url(url)
    

    @allure.step('Клик по кнопке "Конструктор"')
    def click_contsructor_button(self):
        return self.click_to_element(OrderPageLocators.CONSTRUCTOR_BUTTON)
    

    @allure.step('Клик по ингредиенту')
    def click_to_ingredient(self):
        return self.click_to_element(OrderPageLocators.BUN)
    

    @allure.step('Проверка открытия модального окна с информацией об ингредиенте')
    def check_modal_window(self):
        return self.find_element_by_locator(OrderPageLocators.MODAL_WINDOW)
    

    @allure.step('Закрытия модального окна')
    def close_modal_window(self):
        return self.click_to_element(OrderPageLocators.CLOSE_MODAL_WINDOW)
    

    @allure.step('Перетаскивание булочки в конструктор')
    def moving_bun_to_constructor(self):
        return self.moving_element(OrderPageLocators.BUN, OrderPageLocators.CONSTRUCTOR_BURGER)
    
    
    @allure.step('Получение значения из каунтера инредиента')
    def check_counter_ingredient(self):
        return self.get_text_element(OrderPageLocators.COUNTER_INGREDIENT)
    
    
    @allure.step('Клик по кнопке "Соусы"')
    def click_to_sauces_button(self):
        return self.click_to_element(OrderPageLocators.SAUCES_BUTTON)
    

    @allure.step('Перетаскивание соуса в конструктор')
    def moving_souce_to_constructor(self):
        return self.moving_element(OrderPageLocators.SAUCE, OrderPageLocators.CONSTRUCTOR_BURGER)
    

    @allure.step('Клик по кнроке "Начинки"')
    def click_to_toppings_button(self):
        return self.click_to_element(OrderPageLocators.TOPPINGS_BUTTON)
    
    @allure.step('Перетакскивание начинки в конструктор')
    def moving_topping_to_constructor(self):
        return self.moving_element(OrderPageLocators.TOPPING, OrderPageLocators.CONSTRUCTOR_BURGER)


    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_to_create_order_button(self):
        return self.click_to_element(OrderPageLocators.CREATE_ORDER_BUTTON)
    
    
    @allure.step('Проверка открытия модального окна')
    def check_modal_window_with_order_info(self):
        return self.find_element_by_locator(OrderPageLocators.MODAL_WINDOW_WITH_ORDER_INFO)

    
    @allure.step('Ожидание появления id заказа')
    def wait_order_id(self):
        return self.wait_element(OrderPageLocators.ORDER_ID, '9999')

    
    @allure.step('Проверка id заказа')
    def check_order_id(self):
        return self.get_text_element(OrderPageLocators.ORDER_ID)
    
    
    @allure.step('Проверка статуса заказа')
    def check_status_order(self):
        return self.get_text_element(OrderPageLocators.STATUS_ORDER)

    
    allure.step('Закрытие модального окна')
    def close_modal_window_with_order_info(self):
        return self.click_to_element(OrderPageLocators.CLOSE_MODAL_WINDOW_WITH_ORDER_INFO)
    
    
    @allure.step('Создание заказа')
    def create_order(self):
        self.moving_bun_to_constructor()    
        self.click_to_sauces_button()
        self.moving_souce_to_constructor()
        self.click_to_toppings_button()
        self.moving_topping_to_constructor()
        self.click_to_create_order_button()

    