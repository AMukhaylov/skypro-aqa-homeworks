from employee import Company
from employee_table import EmployeeTable

db = EmployeeTable('postgresql://x_clients_user:axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com/x_clients')
api = Company('https://x-clients-be.onrender.com')


def test_get_employee_list():
    company_id = api.get_company_id(3)['id']
    company_employee = api.get_employee_list(params_add={'company': company_id})
    company_employee_db = db.get_employee_list(company_id)
    assert len(company_employee) == len(company_employee_db)


def test_add_employee():
    company_id = api.get_company_id(3)['id']
    body = api.get_employee_list(params_add={'company': company_id})
    len_before = len(body)
    employee = {
        "id": 0,
        "firstName": api.random_First_name(),
        "lastName": api.random_Last_name(),
        "companyId": company_id,
        "phone": api.random_phone(),
        "email": api.random_email(),
        "birthdate": api.random_brthday(),
        "isActive": True
    }
    result = api.add_employee(employee)
    new_id = result["id"]
    body = api.get_employee_list(params_add={'company': company_id})
    len_after = len(body)
    new_employee = api.get_new_employee(new_id)
    max_id = db.get_employee_id(company_id)
    employee_db = db.get_employee(company_id, max_id)
    db.delete(max_id)

    assert len_after - len_before == 1
    assert max_id == new_id
    assert new_employee["id"] == employee_db[0][0]
    assert new_employee["firstName"] == employee_db[0][4]
    assert new_employee["lastName"] == employee_db[0][5]
    assert new_employee["email"] == employee_db[0][8]
    assert new_employee["phone"] == employee_db[0][7]
    assert new_employee["birthdate"] == str(employee_db[0][9])
    assert new_employee["isActive"] == employee_db[0][1]


def test_get_employee():
    company_id = api.get_company_id(3)['id']
    first_name = api.random_First_name()
    last_name = api.random_Last_name()
    phone = api.random_phone()
    db.create(company_id, first_name, last_name, phone)
    max_id = db.get_employee_id(company_id)
    employee_db = db.get_employee(company_id, max_id)
    body = api.get_employee_list(params_add={'company': company_id})
    new_id = max_id
    employee = api.get_new_employee(new_id)
    db.delete(max_id)

    assert employee['id'] == employee_db[0][0]
    assert employee['companyId'] == employee_db[0][11]
    assert employee['firstName'] == employee_db[0][4]
    assert employee['lastName'] == employee_db[0][5]
    assert employee['phone'] == employee_db[0][7]
    assert employee['isActive'] == employee_db[0][1]


def test_edit_employee():
    company_id = api.get_company_id(3)['id']
    first_name = api.random_First_name()
    last_name = api.random_Last_name()
    phone = api.random_phone()
    db.create(company_id, first_name, last_name, phone)
    max_id = db.get_employee_id(company_id)
    api.get_new_employee(max_id)
    last_name = api.random_Last_name()
    e_mail = api.random_email()
    patch = {
        "lastName": last_name,
        "email": e_mail,
        "isActive": False
    }
    result = api.edit_employee(max_id, json=patch)
    employee_db = db.get_employee(company_id, max_id)
    db.delete(max_id)

    assert result["id"] == max_id
    assert result["email"] == employee_db[0][8]
    assert result["isActive"] == False
    assert employee_db[0][1] == False
