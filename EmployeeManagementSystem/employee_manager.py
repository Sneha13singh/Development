try:
    from .employee import Employee
except ImportError:  # pragma: no cover - allows direct script execution
    from employee import Employee


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def find_employee(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                return employee
        return None

    def employee_count(self):
        return len(self.employees)  

    def employee_exists(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                return True
        return False

    def update_salary(self, employee_id, new_salary):
        employee = self.find_employee(employee_id)
        if employee:
            employee.update_salary(new_salary)
        return employee

    def highest_salary_employee(self):
        highest_employee= self.employees[0] if self.employees else None
        for employee in self.employees:
            if employee.salary > highest_employee.salary:
                highest_employee = employee
        return highest_employee

    def average_salary(self):
        total_salary=0
        for employee in self.employees:
            total_salary += employee.salary
        return total_salary / len(self.employees) if self.employees else 0

    def employee_names(self):
        return [employee.name for employee in self.employees]

    def remove_employee_by_id(self, employee_id):
        employee = self.find_employee(employee_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False    

    def get_all_employees(self):
        return self.employees   

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for employee in self.employees:
                file.write(f"{employee.id},{employee.name},{employee.salary}\n")

    def load_from_file(self, filename):
        self.employees=[]
        with open("Employees.txt", 'r') as file:
            content=file.read()
            lines = content.strip().split('\n')
            for line in lines:
                if line=="":
                    continue
                parts=line.split(',')
                employee = Employee(int(parts[0].strip()), parts[1].strip(), float(parts[2].strip()))
                self.employees.append(employee)

    def lowest_salary_employee(self):
        lowest_employee = self.employees[0] if self.employees else None
        for employee in self.employees:
            if employee.salary < lowest_employee.salary:
                lowest_employee = employee
        return lowest_employee

    def employee_above_salary(self, amount):
        l=[]
        for employee in self.employees:
            if employee.salary > amount:
                l.append(employee)
        return l
    
    def search_employee_by_name(self, name):
        l=[]
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                l.append(employee)
        if len(l)==0:
            return None
        return l

    def total_bonus(self):
        total_bonus=0
        for employee in self.employees:
            total_bonus += employee.bonus()
        return total_bonus

    def employee_summary(self):
        return {
            "employee_count": self.employee_count(),
            "highest_salary_employee": self.highest_salary_employee(),
            "lowest_salary_employee": self.lowest_salary_employee(),
            "average_salary": self.average_salary(),
            "total_bonus": self.total_bonus(),
            "employee_names": self.employee_names(),
            "total_salary": sum(employee.salary for employee in self.employees)
        }
