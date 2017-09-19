user_input = raw_input("Enter a word: ")
pyg = 'ay'

#print user_input
#print pyg

#first_letter = user_input[0]
#print first_letter
#middle_string = user_input[1:len(user_input)]
#print middle_string

#latin = middle_string + first_letter + pyg
#print latin

def first_letter(input):
    return input[0]

def bulk_string(input):
    return input[1:len(input)]

def romanize(string, first_letter):
    return string + first_letter + pyg

if len(user_input) != 0 and user_input.isalpha():
    #find first letter
    first = first_letter(user_input)
    middle = bulk_string(user_input)
    print romanize(middle,first)
else:
    print "Please enter a valid word"
