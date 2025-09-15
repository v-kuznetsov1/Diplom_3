from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(self.browser)


    def find_element_by_locator(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))
    

    def click_to_element(self, locator):
        element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        element.click()
        return element
    
   
    def enter_text(self, locator, enter_text):
        field = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))
        field.send_keys(enter_text)
        return field
    

    def get_attribute_element(self, locator, attribute):
        return self.browser.find_element(*locator).get_attribute(attribute)


    def check_current_url(self, url):
        return WebDriverWait(self.browser, 10).until(EC.url_to_be(url))
    

    def moving_element(self, source_element, target_element):
        
        first_element = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(source_element))
        second_element = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(target_element))

        action = self.actions.drag_and_drop(first_element, second_element).perform()

        return action
    

    def get_text_element(self, locator):
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))
        return element.text
    
    
    def wait_element(self, locator, condition):

        default_id = self.find_element_by_locator(locator)
        WebDriverWait(self.browser, 5).until(lambda browser: default_id.text != condition)

        new_id = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        return new_id.text
    

    def click_element_with_condition(self, locator, condition):
        
        element = WebDriverWait(self.browser, 5).until(
        EC.text_to_be_present_in_element(locator, condition)
        )
        element = self.find_element_by_locator(locator)
        return element.click()
    

    def get_text_with_condition(self, locator, condition):
        
        element = WebDriverWait(self.browser, 5).until(
        EC.text_to_be_present_in_element(locator, condition)
        )
        element = self.find_element_by_locator(locator)
        return element.text
        
                                                    
