
import allure
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage
from urls import URLs



class TestPersonalAccount:

    
    @allure.title('Проверка личного кабинета пользователя')
    def test_personal_account(self, browser, login_user):

        main_page = MainPage(browser)
        personal_account = PersonalAccountPage(browser)
        
        
        main_page.click_to_personal_account_button()
        personal_account.click_to_order_history()

        with allure.step('Проверка, что клиент перешел на страницу с историей заказов'):
            assert personal_account.get_expected_url(URLs.ORDER_HISTORY_URL) == True, 'Редирект на /account/order-history не произошел'

        personal_account.click_to_logout_button()

        with allure.step('Проверка, что клиент перешел на страницу авторизации после выхода'):
            assert personal_account.get_expected_url(URLs.LOGIN_PAGE_URL) == True, "Редирект на /login не произошел"

