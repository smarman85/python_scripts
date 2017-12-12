"""
def reverse_word(word):
    # reverse the word:
    reverse = word[::-1]
    return reverse

user_input = input("Please enter a word: ")
if user_input.isalpha():
    reverse_word(user_input)
else:
    print ("Please enter a real word")

if reverse_word(user_input) == user_input:
    print ("You hava a palindrom")
else:
    print ("No luck this time")
"""

def reverse_word(word):
    return word[::-1]

user_input = input("Please enter a word: ")
user_input = user_input.replace(" ", "")

if user_input.isalpha() and user_input != " ":
    if reverse_word(user_input) == user_input:
        print ("Congrats, %s is a palindrom" % user_input)
    else:
        print ("Sorry, %s is not a palindorm" % user_input)
else:
    print ("Please enter a valid word")
