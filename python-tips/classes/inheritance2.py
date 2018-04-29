class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calc_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# parttime employee
class PartTimeEmployee(Employee):
    def calc_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    # use function from the 
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calc_wage(hours)

mia = Employee("Mia")
max = PartTimeEmployee("Max")
milton = PartTimeEmployee("Milton")
print(mia.calc_wage(40))
print(max.calc_wage(40))
print(milton.full_time_wage(40))
