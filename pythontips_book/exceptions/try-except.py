try:
    file = open('test.txt', 'rb')
except IOError as e:
    print("An IOError occurred. {}".format(e.args[-1]))
