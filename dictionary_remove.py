# key - animal_name : value - location 
zoo_animals = {
  'Unicorn' : 'Cotton Candy House',
  'Sloth' : 'Rainforest Exhibit',
  'Bengal Tiger' : 'Jungle House',
  'Atlantic Puffin' : 'Arctic Exhibit',
  'Rockhopper Penguin' : 'Arctic Exhibit'
}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

# Reassign penguin exibit
zoo_animals['Rockhopper Penguin'] = "Tennis court"


print zoo_animals
