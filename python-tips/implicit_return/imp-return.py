# old way 
def foo1(value):
    if value:
        return value
    else:
        return None

# implicit return
def foo2(value):
    """ Bare return statement implies 'return None """
    if value:
        return vaule
    else:
        return

# equivelent as above
def foo3(value):
    """Missing return statement implies 'return None' """
    if value:
        return value


# when to use
# if a function doesn't have a logical return value
