class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_rise(self, annual_salary_raise=5000):
        self.annual_salary += annual_salary_raise




if __name__ == "__main__":
    emp = Employee('smile', 'x', 123456)
    print(emp.annual_salary)
    emp.give_rise(4)
    print(emp.annual_salary)

