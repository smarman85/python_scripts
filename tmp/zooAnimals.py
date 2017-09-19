class Animal(object):
    legs = 2
    isAlive = True

    def __init__(self, specie, age, habitat):
        self.specie  = specie
        self.age     = age
        self.habitat = habitat

    def describe(self):
      return "Hi I am a %s and I live in the %s. I am %d years old. I have %s legs." % (self.specie, self.habitat, self.age, self.legs)

jerry = Animal("Kangaroo", 21, "outback")
print jerry.describe()
