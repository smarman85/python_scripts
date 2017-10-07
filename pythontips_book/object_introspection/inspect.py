import inspect
print inspect.getmembers(str)

# Output:
# Traceback (most recent call last):
#   File "inspect.py", line 1, in <module>
#     import inspect
#   File "/Users/smarman/Documents/repos/python_scripts/pythontips_book/object_introspection/inspect.py", line 2, in <module>
#     print inspect.getmembers(str)
# AttributeError: 'module' object has no attribute 'getmembers'
