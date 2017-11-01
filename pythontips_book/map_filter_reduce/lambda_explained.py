""" 
lambdas are one line functions:
also known as anonymous function in some other languages
might want to use lambdas when you don't want to use a function twice in a program
are like normal functions and even behave like them.
"""

# Blueprint:
# lamda argument: manipulate(argument)

# Ex1
add = lambda x, y: x + y
print (add(3,5))
# Output: 8

#ex2 list sorting
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print (a)
# out: [(13, -3), (4, 1), (1, 2), (9, 10)]

#ext3 parallel sort
data = zip(list1, list2)
data.sort()
list1, list2 = map(lambda t: list(t), zip(*data))
