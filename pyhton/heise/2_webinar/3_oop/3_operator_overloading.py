class Employee:

    def __init__(self, first_name, last_name, zip_code, town, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.zip_code = zip_code
        self.town = town
        self.salary = salary

    def raise_salary(self, percent):
        self.salary *= (1 + percent / 100)

    def __add__(self, other):
        return Employee(self.first_name, self.last_name + '-' + other.last_name, self.zip_code, self.town, (self.salary + other.salary) // 2)

def main():
    employee_hotz = Employee('Alexander', 'Hotz', 4856, 'Murgenthal', 56071)
    employee_moroff = Employee('Anica', 'Moroff', 3285, 'Charmey', 80428)
    print('Before marriage')
    print(f'Name: {employee_hotz.first_name} {employee_hotz.last_name} | Salary: {employee_hotz.salary}')
    print(f'Name: {employee_moroff.first_name} {employee_moroff.last_name} | Salary: {employee_moroff.salary}')
    print()

    print('Marrige')
    employee_hotz_moroff = employee_hotz + employee_moroff
    employee_moroff_hotz = employee_moroff + employee_hotz

    print('After marriage')
    print(f'Name: {employee_hotz_moroff.first_name} {employee_hotz_moroff.last_name} |',
          f'Salary: {employee_hotz_moroff.salary}')
    print(f'Name: {employee_moroff_hotz.first_name} {employee_moroff_hotz.last_name} |',
          f'Salary: {employee_moroff_hotz.salary}')


if __name__ == '__main__':
    main()
