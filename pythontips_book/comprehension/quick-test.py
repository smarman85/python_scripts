def greeting(num):
    print "Hello number: " + str(num)

squared = [greeting(x**2) for x in range(10)]

# output:
# Hello number: 0
# Hello number: 1
# Hello number: 4
# Hello number: 9
# Hello number: 16
# Hello number: 25
# Hello number: 36
# Hello number: 49
# Hello number: 64
# Hello number: 81
