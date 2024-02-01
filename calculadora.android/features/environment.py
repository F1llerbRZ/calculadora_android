from appium import webdriver
from app.application import Application

def before_scenario(context, scenario):
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",
    desired_capabilities={"platformName": "Android",
                            "automationName": "UIAutomator2",
                            "appPackage": "com.google.android.calculator",
                            "appActivity": "com.android.calculator2.Calculator",
                            "platformVersion": "10.0"})

    context.driver.implicitly_wait(30)
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()