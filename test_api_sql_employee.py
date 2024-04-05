
from employeeTable import employeeTable
import datetime
import requests
from employeApi import EmployeeApi
import allure

db_connection_string = "postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet"
url = "https://x-clients-be.onrender.com"
sql = employeeTable(db_connection_string)
api = EmployeeApi(url)


@allure.title("Создание нового сотрудника")
@allure.description("Создание нового сотрудника и проверка,что компания и сотрдуник создались с корректными данными")
@allure.feature("CREATE")
@allure.severity("CRITICAL")
def test_create_new_employee():
    name = "Туры"
    description = "Туры на Сахалин"
    sql.create_company(name, description)
    company_id = sql.get_max_id_company()
    employee_before = sql.get_employee_id(company_id)
    api.add_employee(
        id="3158",
        first_name="Sasha",
        last_name="Morgan",
        middle_name="Ivanovich",
        company_id= company_id,
        mail="datch@example.com",
        employee_url="http://example.com",
        phone="8976493208",
        birthdate= '2024-03-22T12:24:58.028Z',
        is_active=True
    )
    employee_id = sql.get_employee_max_id()
    employee_after = sql.get_employee_id(company_id)
    assert len(employee_after) > len(employee_before)
    with allure.step("Проверка названия компании"):
        assert sql.get_company()[4] == "Туры"

    with allure.step("Проверка описания компании"):
        assert sql.get_company()[5] == "Туры на Сахалин"

    with allure.step("Проверка имени сотрудника"):
        assert sql.get_employee()[-1]["first_name"] == 'Sasha'

    with allure.step("Проверка фамилии сотрудника"):
        assert sql.get_employee()[-1]["last_name"] == 'Morgan'

    with allure.step("Проверка отчества сотрудника"):
        assert sql.get_employee()[-1]["middle_name"] == 'Ivanovich'

    with allure.step("Проверка email сотрудника"):
        assert sql.get_employee()[-1]["email"] == None

    with allure.step("Проверка url сотрудника"):
        assert sql.get_employee()[-1]["avatar_url"] == 'http://example.com'

    with allure.step("Проверка номера телефона сотрудника"):
        assert sql.get_employee()[-1]["phone"] == '8976493208'

    with allure.step("Проверка даты рождения сотрудника"):
        assert sql.get_employee()[-1]["birthdate"] == datetime.date(2024, 3, 22)

    with allure.step("Проверка,что компания имеет статуст True"):
        assert sql.get_employee()[-1]["is_active"] == True
    sql.delete_employee(employee_id)
    sql.delete_company(company_id)

@allure.title("Обновление данных сотрудника")
@allure.description("Обновление некоторых данных сотрудника и проверка,что все данные успешно внесены в БД")
@allure.feature("UPDATE")
@allure.severity("CRITICAL")
def test_change_employee():
    name = "ООО Лянча"
    description = "Итальянские машины"
    sql.create_company(name, description)
    company_id = sql.get_max_id_company()
    sql.get_employee_id(company_id)
    employee = api.add_employee(
        id="3158",
        first_name="Павел",
        last_name="Брашалов",
        middle_name="Дмитриевич",
        company_id= company_id,
        mail="pizza@example.com",
        employee_url="http://ya.ru",
        phone="88709087654",
        birthdate= '2024-03-22T12:24:58.028Z',
        is_active=True
    )
    api.change_employee(
        id = employee,
        change_lastName = "Брюлов" ,
        change_email = "samurai@cyber.ru", 
        change_url = "https://www.google.ru/", 
        change_phone = "89763215423",
        change_active = False
    )
    employee_id = sql.get_employee_max_id()

    with allure.step("Проверка названия компании"):
        assert sql.get_company()[4] == "ООО Лянча"

    with allure.step("Проверка описания компании"):
        assert sql.get_company()[5] == "Итальянские машины"

    with allure.step("Проверка измененной фамилии сотрудника"):
        assert sql.get_employee()[-1]["last_name"] == 'Брюлов'

    with allure.step("Проверка измененного email"):
        assert sql.get_employee()[-1]["email"] =='samurai@cyber.ru'

    with allure.step("Проверка изменненого url"):
        assert sql.get_employee()[-1]["avatar_url"] == 'https://www.google.ru/'

    with allure.step("Проверка измененного номера телефона"):
        assert sql.get_employee()[-1]["phone"] == '88709087654'

    with allure.step("Проверка,что компания имеет статус False"):
        assert sql.get_employee()[-1]["is_active"] == False

    

    sql.delete_employee(employee_id)
    sql.delete_company(company_id)
