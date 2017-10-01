# allows you to pass keyworded variable length of arguments to a
# function. You should use **kwargs if you want to handle named arguments.

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print "{0} = {1}".format(key, value)

greet_me(name="yasoob")
