from app.pages.calculator_page import CalculatorPage
 
 
class Application:
    def __init__(self, driver):
        self.calculator_page = CalculatorPage(driver)