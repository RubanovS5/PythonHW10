from selenium import webdriver
import pytest
from Pages.sauce_login import Login
from Pages.sauce_product import Production
from Pages.sauce_personal import My_personal
from Pages.sauce_result import Sum
import allure
@allure.title("Интернет-магазин")
@allure.description("Добавление товаров в корзину и сравние итоговой суммы")
@allure.feature("Покупка товаров")
@allure.severity("CRITICAL")
def test_sauce():
    browser = webdriver.Chrome()
    log = Login(browser)
    prod = Production(browser)
    personal = My_personal(browser)
    result = Sum(browser)
    log.text("standard_user")
    log.password("secret_sauce")
    log.click()
    prod.product()
    personal.first_name("Александр")
    personal.last_name("Рубанов")
    personal.postal("196784")
    personal.click()
    total_price = result.buy()
    total = 'Total: $58.29'
    with allure.step("Проверка совпадение цены на сайте с ожидаемой ценой"):
        assert total == total_price
        browser.quit()


