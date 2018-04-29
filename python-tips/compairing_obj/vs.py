# is vs ==
# difference between to things being the same and equal

# == checks for equality
# is compaires identities

a = [1,2,3]
b = a
print(a)
print(b)
print( a == b) # prints True
print(a is b) # prints True


print("*****************")

a = [1,2,3]
b = a
c = list(a)
print(a)
print(b)
print(c)
print(a == c) #True ie look the same 
print(a is c) # False are not the same
