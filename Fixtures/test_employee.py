from employee import Employee
import pytest

@pytest.fixture
def employee():
    return Employee('email', 'abdella', 123)

def test_give_default_raise(employee):
    prev_salary = employee.annual_salary
    employee.give_rise()
    assert employee.annual_salary - prev_salary == 5000

def test_custom_raise(employee):
    prev_salary = employee.annual_salary
    salary_advance = 4
    employee.give_rise(salary_advance)
    assert salary_advance == employee.annual_salary - prev_salary