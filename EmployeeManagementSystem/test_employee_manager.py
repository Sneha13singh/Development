import pytest

from EmployeeManagementSystem.employee import Employee
from EmployeeManagementSystem.employee_manager import EmployeeManager

@pytest.fixture
def employee():
    return Employee(id=1101, name="Sneha Singh", salary=90000)

@pytest.fixture
def employee_manager():
    manager=EmployeeManager()
    employee1=Employee(
        102, "Akshay", 80000
    )

    employee2=Employee(
        103, "Rohit", 75000
    )
    manager.add_employee(employee1)
    manager.add_employee(employee2) 
    return manager  

def test_employee_count(employee_manager):
    assert employee_manager.employee_count() == 2

def test_employee_exists(employee_manager):
    assert employee_manager.employee_exists(102) == True
    assert employee_manager.employee_exists(999) == False

def test_find_employee(employee_manager):
    employee = employee_manager.find_employee(102)
    assert employee.name == "Akshay"
    assert employee.salary == 80000

def test_update_salary(employee_manager):
    employee_manager.update_salary(102, 85000)
    employee = employee_manager.find_employee(102)
    assert employee.salary == 85000 

def test_find_employee_not_found(employee_manager):
    employee = employee_manager.find_employee(999)
    assert employee is None

def test_employee_not_exists(employee_manager):
    assert employee_manager.employee_exists(999) == False