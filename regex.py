import re

def disemvowel(string):
    output = ""
    for letter in string:
        match = re.search(r'[AEIOUaeiou]', letter)
        if match:
            pass
        else:
            output = output + letter
    return output
    #return string

print (disemvowel("This website is for losers LOL!"))
