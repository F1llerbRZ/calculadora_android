from app.input import Input
from selenium.webdriver.common.by import By
from base_calculator import Page
 
 
class CalculatorPage(Page):
   
    def click_on_button(self, button):
        self.click_on_element(button)
 
    def get_result(self):
        return self.find_element(Input.RESULT).get_attribute("text")