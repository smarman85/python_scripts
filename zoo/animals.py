animals = ["giraffe", "zebra", "elephant", "lion"]

class Animal(object):

    legs = 4
    alive = True 

    def __init__(self, name):
        self.name = name

    def animal_info(self):
        if self.alive == True:
            status = "alive"
        else:
            status = "Don't ask"
        print "Hello, I am a %s. I have %d legs and I am %s." % (self.name, self.legs, status)

class TwoLegs(Animal):
    legs = 2

# create class
for animal in animals: 
    animal = Animal(animal)
    animal.animal_info()

roo = TwoLegs("kangaroo")
roo.animal_info()

# zebra = Animal("zebra")
# print zebra.legs
# zebra.animal_info()
