def check_pal (word):
    backward = ""
    for i in word[::-1]:
        backward = backward + i
    return (backward)


test_string = input("Enter a word: ")
if test_string.isalpha():
    backward = check_pal(test_string)
    if backward == test_string:
        print ("Congrats you just found a palindrome: %s" % test_string)
    else:
        print ("%s is not a palindrome." % test_string)
else:
    print ("Please enter a valid word.")
