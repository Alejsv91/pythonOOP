from .employee import Employee

name: str = input("Add the employee name: ")
salary: float = input("Add the salary: ")

emp = Employee(name, salary)

promote_employee = input(f"Do you want to promote {emp.name}?: (Y/n)") == "Y"
if promote_employee:
    percentage = input("Add promotion-based salary increase percentage: ")
    emp.promote(percentage)