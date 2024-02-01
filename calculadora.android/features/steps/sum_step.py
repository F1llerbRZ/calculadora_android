from app.buttons import Btn
from behave import *
 
 
@given('a sum operation between two numbers')
def step_impl(context):
    context.app.calculator_page.click_on_button(Btn.ONE)
    context.app.calculator_page.click_on_button(Btn.ZERO)
    context.app.calculator_page.click_on_button(Btn.PLUS)
    context.app.calculator_page.click_on_button(Btn.TWO)
    context.app.calculator_page.click_on_button(Btn.ZERO)
 
 
@when('we press equals button')
def step_impl(context):
    context.app.calculator_page.click_on_button(Btn.EQUALS)
 
 
@then('the calculator displays the result of the sum!')
def step_impl(context):
    result = context.app.calculator_page.get_result()
    assert result == '30'