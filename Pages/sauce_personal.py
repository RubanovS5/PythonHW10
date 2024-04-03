from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
class My_personal:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
   
    @allure.step("Ввод имени - {f_name}")
    def first_name(self,f_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'first-name']"))).send_keys(f_name)
    
    @allure.step("Ввод фамили - {l_name} ")
    def last_name (self,l_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'last-name']"))).send_keys(l_name)
    
    @allure.step("Ввод индекса - {postal}")
    def postal(self,postal):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'postal-code']"))).send_keys(postal)
    
    @allure.step("клик по кнопке после ввода имени,фамилии и индекса")
    def click(self):
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()