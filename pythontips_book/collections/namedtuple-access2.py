from collections import namedtuple

Animal = namedtuple("Animal", "name age type")
perry = Animal(name="perry", age=31, type="cat")

print perry
# Output: Animal(name='perry', age=31, type='cat')

print perry.name
# Output: perry
