class Employee:
    _name: str
    _salary: float
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Employee created")
    
    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self.salary
    
    @salary.setter
    def salary(self, value: float):
        try:
            value = float(value)
            if value < 0:
                raise ValueError("Salary can not be negative")
            self._salary = value
            
        except Exception as e:
            raise ValueError(f"An error happen when try to set the salary value. Error: {e}")
        
    @name.setter
    def name(self, value: str):
        self._name = value
        
    def promote(self, percentage_promotion):
        per = float(percentage_promotion)
        self._salary += (self._salary * per)
        print(f"Congrats! {self.name} after your promotion your salary is: ${self._salary}")
        
name: str = input("Add the employee name: ")
salary: float = input("Add the salary: ")

emp = Employee(name, salary)

promote_employee = input(f"Do you want to promote {emp.name}?: (Y/n)") == "Y"
if promote_employee:
    percentage = input("Add promotion-based salary increase percentage: ")
    emp.promote(percentage)
        

        
        
        
        