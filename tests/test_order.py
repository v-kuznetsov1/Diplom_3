
import allure
from urls import URLs
from pages.order_page import OrderPage





class TestOrderPage:

    @allure.title('Проверка перехода на "Ленту заказов" и конструктора')
    def test_check_order_feed_and_constructor(self, browser, login_user):

        order_page = OrderPage(browser)

        order_page.click_order_feed_button()

        with allure.step('Пророверка, что после клика по кнопке произошел редирект на страницу с лентой заказов'):
            assert order_page.check_current_url(URLs.ORDER_FEED_URL) == True, 'Редирект на /feed не произошел'

        order_page.click_contsructor_button()
        order_page.click_to_ingredient()
        order_page.check_modal_window()
        order_page.close_modal_window()
        order_page.moving_bun_to_constructor()
        
        check_counter = order_page.check_counter_ingredient()

        with allure.step('Проверка увеличение каунтера ингредиента после добавления его добавления в конструктор'):
            assert check_counter == '2', 'Каунтер не учитывает добавление ингредиента'



    @allure.title('Проверка создания заказа')
    def test_create_order(self, browser, login_user):
        
        order_page = OrderPage(browser)

        order_page.moving_bun_to_constructor()    
        order_page.click_to_sauces_button()
        order_page.moving_souce_to_constructor()
        order_page.click_to_toppings_button()
        order_page.moving_topping_to_constructor()

        order_page.click_to_create_order_button()
        order_page.check_modal_window_with_order_info()
        
        order_page.wait_order_id()

        status_order = order_page.check_status_order()

        with allure.step('Проверка статуса заказа в модальном окне'):
            assert status_order == 'Ваш заказ начали готовить', 'В модальном окне не отображается статус заказа'

        