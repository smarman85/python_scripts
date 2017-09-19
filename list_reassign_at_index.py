animals = ["ardvard", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
print animals
print "Duck index = %s" % str(duck_index)
#reassign
animals.insert(duck_index, "cobra")
print animals
