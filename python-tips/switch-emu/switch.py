# use first class functions

def myfunc(a, b):
    return a + b

funcs = [myfunc]
print(funcs[0](2,3))



# can use a dict to store handles
func_dict = {
        'cond_a' : handle_a,
        'cond_b' : handle_b,
        }
func_dict.get(cond, handle_default)()
#              ^ get value if defined or else call handle_default func. Will avoid a keyError
# faster than if else cause it doesn't have to check every condition
# extremely helpful for a large set of conditions

# cleaner implementation

# old if elif else
def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y

dispatch_if('mul', 2, 8)

# same func with dictionary switch emulation
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

# creates dict and uses lambda to keep behavior inline. 
# !! genrate a dict every time it's called. Bad for memeory 
# would be better to store as a variable elsewhere
# advanced python
