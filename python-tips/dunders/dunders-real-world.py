class Car: 
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # recommmened to put a dunder repr method on all classes you 
    # define. Get a helpful and readable result
    def __repr__(self):
        return '{self.__class__.__name__}({self.color}, {self.mileage})'.format(self=self)
        #         ^ grabs the name of the class so you don't have to

my_car = Car('red', 654654)
print(my_car)
print(str(my_car)) # str calls repr internally


# at the very least add a __repr__ to all your classes
