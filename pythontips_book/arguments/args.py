# args mostly used in function definitions allow you 
# to pass a variable number of arguments to a function.
# *args is used to send in non-keyworded variable length
# argument list to the function

def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg 
    for arg in argv:
        print "Another arg through *argv:", arg 

test_var_args('yasoob', 'python', 'eggs', 'test')
