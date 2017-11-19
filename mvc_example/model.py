import json

class Person(object):
    def __init__(self, first_name = None, last_name = None):
        self.first_name = first_name
        self.last_name = last_name

    #returns Person name, ex: John Doe
    def name(self):
        return ("{0} {1}".format(self.first_name, self.last_name))
        
    @classmethod
    def getAll(self):
        database = open('db.txt', 'r')
        result = []
        for item in database:
            result.append(item)
        return result
