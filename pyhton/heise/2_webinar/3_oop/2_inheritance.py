class Employee:

    def __init__(self, first_name: str, last_name, zip_code, town, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.zip_code = zip_code
        self.town = town
        self.salary = salary
    
    def raise_salary(self, percent):
        self.salary *= (1 + percent / 100)

class Developer(Employee):
    def __init__(self, first_name: str, last_name, zip_code, town, salary, main_language, loc_per_day):
        super().__init__(first_name, last_name, zip_code, town, salary)
        self.main_language = main_language
        self.loc_per_day = loc_per_day

    def calculate_salary_per_loc(self):
        return self.salary / 240 / self.loc_per_day # 240 is average number of working days per year

def main():
    employee_hotz = Employee('Alexander', 'Hotz', 4856, 'Murgenthal', 56071)
    employee_moroff = Developer('Anica', 'Moroff', 3285, 'Charmey', 80428, "python", 1000)
    print(f'Name: {employee_hotz.first_name} {employee_hotz.last_name} | Salary: {employee_hotz.salary}')
    employee_hotz.raise_salary(5)
    print(f'Name: {employee_hotz.first_name} {employee_hotz.last_name} | Salary: {employee_hotz.salary}')
    print(f'Salary Difference: {(employee_moroff.salary - employee_hotz.salary):.2f}')
    print(f'Salary per loc: {employee_moroff.calculate_salary_per_loc()}')


    # can be edited everywhere
    employee_moroff.hair_color = "brown"
    print(f'Hair color of Anica', employee_moroff.hair_color)
    # employee_moroff.raise_salary = lambda (self, x): self.salary = x # this does not work, but it is possible to overwrite methods


if __name__ == '__main__':
    main()
