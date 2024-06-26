from sqlalchemy import create_engine
from sqlalchemy.sql import text
import psycopg2
import allure

class employeeTable:
    __scripts = {
        "get company": text("select * from company"),
        "get employee": text("select * from employee"),
        "max id employee": text("select max(id) from employee"),
        "get employee id": text("select * from employee where company_id = :company_id"),
        "insert company": text("insert into company (\"name\", \"description\") values (:new_name, :nem_descr)"),
        "max id company": text("select max(id) from company"),
        "delete company": text("delete from company where id = :id_delete"),
        "delete employee": text("delete from employee where id = :id_delete"),
        "create employee": text("INSERT INTO employee (\"is_active\", \"create_timestamp\",\"change_timestamp\",\"first_name\",\"last_name\",\"middle_name\",\"phone\",\"email\",\"avatar_url\", \"company_id\") values (:is_active, :create_timestamp, :change_timestamp, :first_name, :last_name, :middle_name, :phone, :email, :avatar_url, :company_id)"),
        "update employee" : text("UPDATE employee SET \"is_active\" = :is_active, \"last_name\" = :last_name, \"phone\" = :phone, \"email\" = :email, \"avatar_url\" = :avatar_url WHERE company_id = :company_id")
    }
    
    

    def __init__(self,connection_string):
        self.db = create_engine(connection_string)
    @allure.step("БД.Получение списка компаний")
    def get_company(self):
        with self.db.connect() as conn:
            return conn.execute(self.__scripts["get company"]).fetchall()
    
    @allure.step("БД.Получение списка сотрудников")
    def get_employee(self):
        with self.db.connect() as conn:
            return conn.execute(self.__scripts["get employee"]).fetchall()
    
    @allure.step("БД.Получение сотрудника по ID - {company_id}")
    def get_employee_id(self, company_id):
        with self.db.connect() as conn:
            return conn.execute(self.__scripts["get employee id"],company_id = company_id).fetchall()
    
    @allure.step("БД.Получение сотрудника с максимальным ID")
    def get_employee_max_id(self):
        with self.db.connect() as conn:
            return conn.execute(self.__scripts["max id employee"]).fetchall()[0][0]
    
    @allure.step("БД.Созадние компании {name}({description})")
    def create_company(self,name,description):
        with self.db.connect() as conn:
            conn.execute(self.__scripts["insert company"],new_name = name, nem_descr = description)

    @allure.step("БД.Удаление компании по ID - {id}")
    def delete_company(self, id):
        with self.db.connect() as conn:
            conn.execute(self.__scripts["delete company"], id_delete = id)

    @allure.step("БД.Удаление сотрудника по  ID - {id}")
    def delete_employee(self, id):
        with self.db.connect() as conn:
            conn.execute(self.__scripts["delete employee"], id_delete = id)
                        
    @allure.step("БД.Получение компании с максимальным  ID")
    def get_max_id_company(self):
        with self.db.connect() as conn:
            return conn.execute(self.__scripts["max id company"]).fetchall()[0][0]
    
    @allure.step("БД.Cоздание сотрудника")
    def create_employee(self, is_active, create_timestamp, change_timestamp,  first_name, last_name, middle_name, phone, email, avatar_url, company_id):
        with self.db.connect() as conn:
            conn.execute(self.__scripts["create employee"], is_active = is_active, create_timestamp = create_timestamp, change_timestamp = change_timestamp, first_name = first_name, last_name = last_name, middle_name = middle_name, phone = phone, email = email, avatar_url = avatar_url, company_id = company_id)

    @allure.step("БД.Изменение сотрудника")
    def change_employee(self, is_active, last_name, phone, email, avatar_url, company_id):
        with self.db.connect() as conn:
            conn.execute(self.__scripts["update employee"], is_active = is_active, last_name = last_name, phone = phone, email = email, avatar_url = avatar_url, company_id = company_id)
