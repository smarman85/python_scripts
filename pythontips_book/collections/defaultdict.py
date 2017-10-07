from collections import defaultdict

colors = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
)

favorite_colors = defaultdict(list)

for name, color in colors:
    favorite_colors[name].append(color)

print favorite_colors

# output
# defaultdict(<type 'list'>,
#    {'Arham': ['Green'],
#     'Yasoob': ['Yellow', 'Red'],
#     'Ahmed': ['Silver'],
#     'Ali': ['Blue', 'Black']
# })
