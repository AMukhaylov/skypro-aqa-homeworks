import requests
import random


class Company:

    def __init__(self, url):
        self.url = url

    def random_First_name(self):
        first_name = ['Ivan', 'Petr', 'Sidor', 'Test', 'Kasha', 'Palto', 'Vovaadiddas', 'Zima', 'Maratik']
        return random.choice(first_name)

    def random_Last_name(self):
        last_name = ['Ivanov', 'Petrov', 'Sidorov', 'Testov', 'Kashin', 'Kvartashvili', 'Tatarinov', 'Inozemcev']
        return random.choice(last_name)
    
    def random_email(self):
        e_mail = ['test1@test.com', 'test2@test.com', 'test3@test.com']
        return random.choice(e_mail)
    
    def random_brthday(self):
        birthDay = ['1989-09-15', '1989-09-16']
        return random.choice(birthDay)
    
    def random_phone(self):
        phoneNumber = ['+79922211199', '+79922211198']
        return random.choice(phoneNumber)
    
    def get_company_id(self, int, params_add = None):
        resp = requests.get(self.url + '/company', params=params_add)
        lst = [i for i in resp.json()]
        return lst[int]
    
    def get_token(self, user='donatello', password='does-machines'):
        ident = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url+'/auth/login', json=ident)
        return resp.json()["userToken"]
    
    def get_employee_list(self,params_add = None):
        resp = requests.get(self.url + '/employee', params=params_add)
        return resp.json()
    
    def add_employee(self, json=None):
        if json is None:
            json = {}
        employee = json
        my_head = {"x-client-token": self.get_token()}
        resp = requests.post(self.url+'/employee', json=employee, headers=my_head)
        return resp.json()
    
    def get_new_employee(self, new_id):
        resp = requests.get(self.url+'/employee/' + str(new_id))
        return resp.json()
    
    def edit_employee(self, new_id, json=None):
        if json is None:
            json = {}
        patch = json
        my_head = {"x-client-token": self.get_token()}
        resp = requests.patch(self.url+'/employee/' + str(new_id), json=patch, headers=my_head)
        return resp.json()