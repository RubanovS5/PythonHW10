from Pages.numbers_calculator import Numbers
from selenium import webdriver
import pytest
import allure
@allure.title("Калькулятор")
@allure.description("Установка таймера появления ответа и получение результатов вычеслений")
@allure.feature("Выполение математических вычеслений")
@allure.severity("CRITICAL")
def test_form():
    browser = webdriver.Chrome()
    calculator = Numbers(browser)
    calculator.id_delay('45')
    calculator.actions_calculator()
    calculator.action_result()
    to_be = calculator.action_result()
    as_is = calculator.search_answers()
    with allure.step("Провека,что оба результата равны"):
        assert as_is == to_be


