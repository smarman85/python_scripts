class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

full = Employee("Carl")
print full.calculate_wage(40)
full2 = Employee("Lenny")
print full.calculate_wage(32)
part = PartTimeEmployee("Sean")
print part.calculate_wage(21)
