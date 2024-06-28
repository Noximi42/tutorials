import json as json
from xml.etree.ElementTree import indent


class Employee:

    def __init__(self, first_name, last_name, zip_code, town, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.zip_code = zip_code
        self.town = town
        self.salary = salary

    def raise_salary(self, percent):
        self.salary *= (1 + percent / 100)

class EmployeeJSONEncoder(json.JSONEncoder):

    def default(self, employee):
        if isinstance(employee, Employee):
             return {'_type_': 'Employee',
                     'first_name': employee.first_name,
                     'last_name': employee.last_name,
                     'zip_code': employee.zip_code,
                     'town': employee.town,
                     'salary': employee.salary}
        else:
            return super().default(employee) # Raises type error

class EmployeeJSONDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=EmployeeJSONDecoder.hook, *args, **kwargs)

    @staticmethod
    def hook(employee_json):
        if '_type_' in employee_json and employee_json['_type_'] == 'Employee': 
             return Employee(employee_json['first_name'],
                             employee_json['last_name'],
                             employee_json['zip_code'],
                             employee_json['town'],
                             employee_json['salary'])
        else:
            return employee_json


def main():
    employee_1 = Employee('Alexander', 'Hotz', 4856, 'Murgenthal', 56071)
    print(f'Name: {employee_1.first_name} {employee_1.last_name} | Salary: {employee_1.salary}')
    json_dump = json.dumps(employee_1, cls=EmployeeJSONEncoder, ensure_ascii=False, indent=2)
    print(json_dump)

    print('-' * 100)

    employee_2 = json.loads(json_dump, cls=EmployeeJSONDecoder)
    print(type(employee_2))
    print(f'Name: {employee_2.first_name} {employee_2.last_name} | Salary: {employee_2.salary}')

    print('-' * 100)

    with open('menu_dump.json', mode='rt') as json_file:
        employee_3 = json.load(json_file, cls=EmployeeJSONDecoder)
        print(type(employee_3))
        print(employee_3)


if __name__ == '__main__':
    main()
