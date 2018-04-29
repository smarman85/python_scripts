# *args and **kwargs

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

#foo() # missing args
foo('hello')
#hello
foo('hello', 1, 2, 3)
#hello
(1, 2, 3)
foo('hello', 1, 3, 4, key1='value', key2=999)
#hello
#(1, 3, 4)
#{'key1': 'value', 'key2': 999}


def foo(x, *args, **kwargs):
    kwargs['name'] = "Alice"
    new_args = args + ('extra', )
    bar(x, *new_args, **kwargs)


