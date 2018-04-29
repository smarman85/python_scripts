class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'

my_car = Car('red', 754354)
print(my_car) # __str__ for Car
print(repr(my_car))  # __repr__ for Car

# __str__ vs __repr__
import datetime
today = datetime.date.today()

print(str(today))
# 2018-04-28
print(repr(today))
# datetime.date(2018, 4, 28) 

# __str__ ===> easy to read, for human consumption
# __repr__ ==> unambiguous. show exactly how info was generated. For developers
