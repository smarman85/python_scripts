#word = input("Please enter a word to check: ")
#if word == word[::-1]:
#    print ("Yay")
#else:
#    print ("moron")

word = input("Word Please: ")
if len(word) > 0 and word.isalpha():
    print ("Proceed")
    count = len(word) - 1
    reverse = ""
    while count >= 0:
        reverse = reverse + word[count]
        count -= 1

if reverse == word:
    print("Yay, which is also a palindrom!:)")
else:
    print("Not your lucky day.")
