add = lambda x, y: x + y
print (add(3, 5))

# list sorting:
a = [(1,2), (4,1), (9,10), (13,-3)]
a.sort(key=lambda x: x[1])
print (a)

# parallel sorting of lists:
#data = zip(list1, list2)
#data.sort()
#list1, list2 = map(lambda t: list(t), zip(*data))

# square with lambda
numbers = [x for x in range(10)]
squared = list(map(lambda number: number * number, numbers))

print(squared)
