
import pytest
import allure
import requests as r
from selenium import webdriver
from urls import URLs
from helpers import generate_user_data
from pages.authorization_page import AuthorizationPage
from pages.main_page import MainPage



@pytest.fixture(params=('chrome', 'firefox'))
def browser(request):
    browser_name = request.param
    driver_instance = None

    if browser_name == 'chrome':
        driver_instance = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver_instance = webdriver.Firefox() 
        
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(10)
    driver_instance.get(URLs.BASE_URL)

    yield driver_instance

    if driver_instance:
        driver_instance.quit()




@pytest.fixture(scope="function")
def create_and_delete_user():
    
    payload = generate_user_data()
    response = r.post(URLs.REGISTER_URL, json=payload)
    
    yield response, payload
    
    access_token = response.json()['accessToken']
    with allure.step('Удаление созданного для теста пользователя'):
        r.delete(URLs.USER_URL, headers={'Authorization': access_token})



@pytest.fixture(scope="function")
def login_user(browser, create_and_delete_user):

    response, payload = create_and_delete_user
    email = payload['email']
    password = payload['password']
    main_page = MainPage(browser)
    authorization = AuthorizationPage(browser)
    main_page.click_to_personal_account_button()
    authorization.login(email, password)

    