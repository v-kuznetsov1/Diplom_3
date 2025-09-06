
import allure
from pages.recovery_page import RecoveryPage

class TestRecoveryPassword:


    @allure.title('Проверка страницы восстановления пароля')
    def test_recovery_password(self, browser):

        recovery_page = RecoveryPage(browser)

        recovery_page.click_personal_account_button()
        recovery_page.click_to_recovery_password_button()
        recovery_page.enter_email()
        recovery_page.click_to_recovery_button()
        recovery_page.click_to_hide_button()
        
        with allure.step('Проверка, что клик по кнопке показать/скрыть делает поле активным - подсвечивает его'):
            assert 'input_status_active' in recovery_page.get_show_password()

