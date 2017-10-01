def generator_func():
    for i in range(3):
        yield i

gen = generator_func()
print next(gen)
print next(gen)
print next(gen)
print next(gen)

""" Output:
    0
    1
    2
    Traceback (most recent call last):
      File "next.py", line 9, in <module>
          print next(gen)
          StopIteration
"""
# Error returned when all iterations are shown
