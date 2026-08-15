import pytest

from EmployeeManagementSystem.employee import Employee



@pytest.fixture
def employee():
    return Employee(id=1101, name="Sneha Singh", salary=90000)

def test_employee_str(employee):    
    assert employee.bonus() == 9000.0

def test_high_salary(employee):
    assert employee.is_high_salary() == True

def test_update_name(employee):
    employee.update_name("Sneha S")
    assert employee.name == "Sneha S"   

def test_increase_salary(employee):
    employee.increase_salary(10)
    assert employee.salary == 99000.0

def test_update_salary(employee):
    employee.update_salary(95000)
    assert employee.salary == 95000