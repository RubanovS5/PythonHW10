
from selenium.webdriver.common.by import By
import allure
class Input_field:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    @allure.step("Ввод имени - {first_name}")
    def first_name(self, first_name):
        self.driver.find_element(By.XPATH, "//input[@name='first-name']").send_keys(first_name)

    @allure.step("Ввод фамилии - {last_name}")
    def last_name(self, last_name):
        self.driver.find_element(By.XPATH, "//input[@name='last-name']").send_keys(last_name)

    @allure.step("Ввод адреса - {address}")
    def address(self, address):
        self.driver.find_element(By.XPATH, "//input[@name='address']").send_keys(address)

    @allure.step("Ввод индекса - {zip_code}")
    def zip_code(self, zip_code):
        self.driver.find_element(By.XPATH, "//input[@name='zip-code']").send_keys(zip_code)

    @allure.step("Ввод города - {city}")
    def city(self, city):
        self.driver.find_element(By.XPATH, "//input[@name='city']").send_keys(city)

    @allure.step("Ввод страны - {country}")
    def country(self, country):
        self.driver.find_element(By.XPATH, "//input[@name='country']").send_keys(country)

    @allure.step("Ввод email - {mail}")
    def mail(self, mail):
        self.driver.find_element(By.XPATH, "//input[@name='e-mail']").send_keys(mail)

    @allure.step("Ввод телефона - {phone}")
    def phone(self, phone):
        self.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys(phone)

    @allure.step("Ввод должности - {job}")
    def job(self, job):
        self.driver.find_element(By.XPATH, "//input[@name='job-position']").send_keys(job)

    @allure.step("Ввод названия компании - {company}")
    def company(self, company):
        self.driver.find_element(By.XPATH, "//input[@name='company']").send_keys(company)

    @allure.step("Нажатие кнопки Submit")
    def button(self):
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    @allure.step("Определение цвета поля имени")
    def colour_first_name(self):
        background_color = self.driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
        return background_color
    
    @allure.step("Определение цвета поля фамилии")
    def colour_last_name(self):
        background_color = self.driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color")
        return background_color
    
    @allure.step("Определение цвета поля адреса")
    def colour_address(self):
        background_color = self.driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color")
        return background_color

    @allure.step("Определение цвета поля индекса")
    def colour_zip_code(self):
        background_color = self.driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        return background_color
    
    @allure.step("Определение цвета поля города")
    def colour_city(self):
        background_color = self.driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color") 
        return background_color
    
    @allure.step("Определение цвета поля страны")
    def colour_country(self):
        background_color = self.driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color")
        return background_color
    
    @allure.step("Определение цвета поля email")
    def colour_mail(self):
        background_color = self.driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color")
        return background_color
    
    @allure.step("Определение цвета поля номера телефона")
    def colour_phone(self):
        background_color = self.driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color")
        return background_color
    
    @allure.step("Определение цвета поля должности")
    def colour_job(self):
        background_color = self.driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color") 
        return background_color
    
    @allure.step("Определение цвета поля компании")
    def colour_company(self):
        background_color = self.driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color") 
        return background_color
    

  

  
      


    
