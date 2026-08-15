class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.id}, Name: {self.name}, Salary: {self.salary}"

    def update_name(self, new_name):
        self.name = new_name
        return f"Employee name updated to: {self.name}"
    
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)
        return f"Employee salary increased to: {self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary

    def bonus(self):
        return self.salary * 0.1  # Assuming a 10% bonus for simplicity

    def is_high_salary(self):
        return self.salary >=50000

    def employee_report(self):
        return f"Employee Report:\nID: {self.id}\nName: {self.name}\nSalary: {self.salary}"