cypher = {
        'a' : '@',
        'e' : '3',
        'i' : '1',
        'o' : '0',
        'l' : '!',
        'g' : '6',
        's' : '5'
}

def encrypt(string):
    encrypted_string = ""
    for letter in string:
        try:
            cypher[letter]
        except KeyError as e:
            encrypted_string = encrypted_string + letter
        else:
            encrypted_string = encrypted_string + cypher[letter]
    return encrypted_string

user_input = input("Please Enter a string: \n")
new_string = encrypt(user_input)
print (new_string)
