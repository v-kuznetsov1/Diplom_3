
import allure
from pages.recovery_page import RecoveryPage
from pages.main_page import MainPage

class TestRecoveryPassword:


    @allure.title('Проверка страницы восстановления пароля')
    def test_recovery_password(self, browser):

        main_page = MainPage(browser)
        recovery_page = RecoveryPage(browser)

        main_page.click_to_personal_account_button()
        recovery_page.click_to_recovery_password_button()
        recovery_page.enter_email()
        recovery_page.click_to_recovery_button()
        recovery_page.click_to_hide_button()
        
        with allure.step('Проверка, что клик по кнопке показать/скрыть делает поле активным - подсвечивает его'):
            assert 'input_status_active' in recovery_page.get_show_password()

