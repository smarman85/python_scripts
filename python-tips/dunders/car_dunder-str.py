class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # dunder methods start with __ 'double underscore'
    # returns color of car when called
    # controll how an object is represented as a string
    def __str__(self):
        return 'a {self.color} car'.format(self=self)

my_car = Car('red', 37845)
print(my_car)
# <__main__.Car object at 0x101999c88>   without the __str__ method
# a red car with the __str__ method
