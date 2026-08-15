import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

conn = psycopg.connect(
    os.getenv("DATABASE_URL")
)

curr = conn.cursor()

def update_salary(employee_id, new_salary):
    curr.execute("UPDATE employees SET salary = %s WHERE id = %s", (new_salary, employee_id))
    conn.commit()

def delete_employee(employee_id):
    curr.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
    conn.commit()

def find_employee(employee_id):
    curr.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
    return curr.fetchone()

def add_employee(employee):
    curr.execute("INSERT INTO employees (id, name, salary) VALUES (%s, %s, %s)", (employee.id, employee.name, employee.salary))
    conn.commit()   

def get_all_employees():
    curr.execute("SELECT * FROM employees")
    return curr.fetchall()

curr.close()
conn.close()