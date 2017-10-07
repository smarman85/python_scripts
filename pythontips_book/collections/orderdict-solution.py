from collections import OrderedDict

colors = OrderedDict([("Red", 198), ("Green", 170),("Blue", 160)])
for key, value in colors.items():
    print key, value

# Output:
#   Red 198
#   Green 170
#   Blue 160
# Insertion order is preserved
