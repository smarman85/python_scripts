class Fruit(object):
    """A class that makes various tasty fruits"""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print("I'm a {0} {1} adn I taste {2}.".format(self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print ("Yep, eat me!")
        else:
            print ("Think again loser")

lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
lemon.is_edible()
