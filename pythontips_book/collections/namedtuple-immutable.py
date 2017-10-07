from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
perry.age = 42 # wont work cause it's immutable
#output:
#Traceback (most recent call last):
#      File "namedtuple-immutable.py", line 5, in <module>
#          perry.age = 42 # wont work cause it's immutable
#          AttributeError: can't set attribute
