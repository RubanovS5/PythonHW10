from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
class Login:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввод логина")
    def text(self,text):
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(text)
            
    @allure.step("Ввод пароля")
    def password(self,password):
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

    @allure.step("Клик по кнопке после ввода логина и пароля")
    def click(self):
        self.driver.find_element(By.XPATH,"//input[@id='login-button']").click()