from sqlalchemy import create_engine
from sqlalchemy import text


class EmployeeTable:
    query = {
        'list SELECT': text('select * from employee where company_id = :id'),
        'item SELECT': text('select * from employee where company_id = :c_id and id = :e_id'),
        'maxID SELECT': text('select MAX(id) from employee where company_id = :c_id'),
        'item DELETE': text('delete from employee where id = :id_delete'),
        'item INSERT': text(
            'insert into employee(company_id, first_name, last_name, phone) values(:id, :name, :surname, :phone_num)'
            )
    }

    def __init__(self, engine):
        self.db = create_engine(engine)

    def get_employee_list(self, company_id):
        with self.db.connect() as conn:
            result = conn.execute(
                self.query['list SELECT'], 
                parameters=dict(id=company_id)
                ).fetchall()
            return result
        
    def get_employee(self, company_id, employee_id):
        with self.db.connect() as conn:
            result = conn.execute(
                self.query['item SELECT'], 
                parameters=dict(c_id=company_id, e_id=employee_id)
                ).fetchall()
            return result
        
    def get_employee_id(self, company_id):
        with self.db.connect() as conn:
            result = conn.execute(
                self.query['maxID SELECT'], 
                parameters=dict(c_id=company_id)
                ).fetchall()[0][0]
            return result
        
    def delete(self, id):
        with self.db.connect() as conn:
            result = conn.execute(
                self.query['item DELETE'], 
                parameters=dict(id_delete=id)
                )
            conn.commit()
            return result
        
    def create(self, company_id, first_name, last_name, phone):
        with self.db.connect() as conn:
            result = conn.execute(
                self.query['item INSERT'], 
                parameters=dict(id=company_id, name=first_name, surname=last_name, phone_num=phone)
                )
            conn.commit()
            return result


