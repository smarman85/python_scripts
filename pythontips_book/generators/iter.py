#int_var = 1779
#iter(int_var)
# Traceback (most recent call last):
#   File "iter.py", line 2, in <module>
#     iter(int_var)
# TypeError: 'int' object is not iterable

my_string = "Yasoob"
my_iter = iter(my_string)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)

""" Output:
Y
a
s
o
o
b
Traceback (most recent call last):
  File "iter.py", line 16, in <module>
    print next(my_iter)
StopIteration
"""
