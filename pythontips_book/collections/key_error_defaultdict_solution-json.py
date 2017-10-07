import collections
import json
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict["colors"]["favorite"] = "yellow"
dict_json = json.dumps(some_dict)
print dict_json
# Works fine
