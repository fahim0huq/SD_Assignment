class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10  

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20  

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.15  

emp1 = Employee("Fahim", 110, 50000)
emp2 = Manager("Moon", 122, 70000)
emp3 = Developer("Ovi", 133, 60000)

print(f"{emp1.name}'s Bonus: {emp1.calculate_bonus()}")  
print(f"{emp2.name}'s Bonus: {emp2.calculate_bonus()}")  
print(f"{emp3.name}'s Bonus: {emp3.calculate_bonus()}") 
