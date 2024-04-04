from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class Sum:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Подсчет суммы покупок")
    def buy(self):
        price = WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))).text
        return(price)
    
    @allure.step("Выход из браузера")
    def quit(self):
        self.driver.quit()
