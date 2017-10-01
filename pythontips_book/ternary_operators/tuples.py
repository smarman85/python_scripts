# not very pythonic and easy to confuse 
# also both conditions get evaluated, unlike the ternary
# (if_test_is_false, if_test_is_true)[test]
fat = True
fitness = ("skinny", "fat")[fat]
print "Ali is", fitness
