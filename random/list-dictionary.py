# list:
animals = ["Puffin", "Sloth", "Burmese Python", "African Tree Frog"]
animals_dict = {}

def dictionary_from_list(animals):
    for animal in animals:
        if ' ' in animal:
            # turns animal into list of characters
            temp_list = list(animal)
            counter = 0
            for char in temp_list:
                if char != " ":
                    counter += 1
            animals_dict[animal] = counter
        else:
            animals_dict[animal] = len(animal)
    return animals_dict

def add_animal(name):
    if len(name) > 0 and name.isalpha():
        animals.append(name)

print animals
add_animal("Lion")
print animals
zoo = dictionary_from_list(animals)
print zoo
