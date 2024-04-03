from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class Numbers:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    @allure.step("Установление времени для таймера")
    def id_delay(self,time):
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(time)

    @allure.step("Ввод нужных значений в калькулятор")
    def actions_calculator(self):
        self.driver.find_element(By.XPATH,"//span[text()='7']").click()
        self.driver.find_element(By.XPATH,"//span[text()='+']").click()
        self.driver.find_element(By.XPATH,"//span[text()='8']").click()
        self.driver.find_element(By.XPATH,"//span[text()='=']").click()
    
    @allure.step("Ожидание появления результата в поле ответа,по истечению таймера")
    def action_result(self):
        WebDriverWait(self.driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    @allure.step("Результат работы калькулятора")
    def search_answers(self):
        self.driver.find_element(By.CLASS_NAME, "screen").text
      
       

 