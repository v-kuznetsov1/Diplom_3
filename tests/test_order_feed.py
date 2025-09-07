
import allure
from pages.order_page import OrderPage
from pages.order_feed_page import OrderFeed
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage



class TestOrderFeed:

    @allure.title('Проверка ленты заказов')
    @allure.description('Тест на проврерку ленты заказов, счетчиков заказов и нахождение заказа в истории')
    def test_order_feed(self, browser, login_user):

        main_page = MainPage(browser)
        feed_page = OrderFeed(browser)
        order_page = OrderPage(browser)
        personal_account = PersonalAccountPage(browser)
        
        main_page.click_to_order_feed_button()
        
        total_orders = int(feed_page.check_total_orders())
        today_orders = int(feed_page.check_count_orders_today())
        
        main_page.click_to_contructor_button()
        order_page.create_order()
        order_id = order_page.wait_order_id()
        order_page.close_modal_window_with_order_info()

        main_page.click_to_order_feed_button()
        order_in_progress = feed_page.check_order_in_progress()
        
        with allure.step('Проверка, что созданный заказ находится в работе'):
            assert order_in_progress == '0'+order_id

        with allure.step('Проверка, что общее количество заказов увеличилось на +1 созданный заказ'):
            assert (total_orders + 1) - total_orders == 1
        
        with allure.step('Проверка, что количество заказов за день увеличилось на +1 созданный заказ'):
            assert (today_orders + 1) - today_orders == 1
        
        feed_page.click_to_order(order_id)
        feed_page.check_bun_in_order()
        feed_page.check_souce_in_order()
        feed_page.check_topping_in_order()
        feed_page.close_modal_window_with_order_info()
        main_page.click_to_personal_account_button()

        personal_account.click_to_order_history()
        
        with allure.step('Проверка, что созданный заказ отображается в ленте и истории заказов'):
            assert feed_page.check_order_in_orders_history(order_id) == '#0'+order_id, 'Заказ отсуствует в истории заказов'
        
        