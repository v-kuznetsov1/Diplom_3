
import pytest
import allure
import requests as r
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from urls import URLs
from helpers import generate_user_data
from pages.authorization_page import AuthorizationPage



@pytest.fixture(params=('chrome', 'firefox'))
def browser(request):
    browser_name = request.param
    driver_instance = None

    try:
        if browser_name == 'chrome':
            driver_instance = webdriver.Chrome()
        elif browser_name == 'firefox':
            driver_instance = webdriver.Firefox() 
        else:
            raise ValueError(f'Unsupported browser: {browser_name}') 

        driver_instance.maximize_window()
        
        driver_instance.implicitly_wait(10)
        driver_instance.get(URLs.BASE_URL)

        yield driver_instance

    except WebDriverException as e:
        pytest.fail(f"Failed to start {browser_name} browser: {e}")
    
    finally:
        if driver_instance:
            driver_instance.quit()




@pytest.fixture(scope="function")
def create_and_delete_user():
    
    payload = generate_user_data()
    response = r.post(URLs.REGISTER_URL, json=payload)
    
    try:
        yield response, payload
    
    finally:
        access_token = response.json()['accessToken']
        with allure.step('Удаление созданного для теста пользователя'):
            r.delete(URLs.USER_URL, headers={'Authorization': access_token})



@pytest.fixture(scope="function")
def login_user(browser, create_and_delete_user):

    response, payload = create_and_delete_user
    email = payload['email']
    password = payload['password']
    authorization = AuthorizationPage(browser)
    authorization.login(email, password)
    yield authorization

    