import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict["colors"]["favorite"] = "yellow"
print some_dict["colors"]["favorite"] 
# Works fine
