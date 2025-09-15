from selenium.webdriver.common.by import By


class MainPageLocators:

   PERSONAL_ACCOUNT_BUTTON = [By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"]
   ORDER_FEED_BUTTON = [By.XPATH, '//p[text()="Лента Заказов"]']
   CONSTRUCTOR_BUTTON = [By.XPATH, '//p[text()="Конструктор"]']
