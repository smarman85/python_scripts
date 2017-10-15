def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# first with *args
# dont need to be named args but needs to run with "*" before the variable name
args = ("two", 3, 5)
print("Args")
test_args_kwargs(*args)

# now with **kwargs:
# dont need to be named kwargs but needs to run with "*" before the variable name
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
print("Kwargs")
test_args_kwargs(**kwargs)

# can run all three with:
# sum_func(fargs, *args, **kwargs)
