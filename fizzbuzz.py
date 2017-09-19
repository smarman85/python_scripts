string = ""
for num in range(1,101):
    if num % 2 == 0:
        string = string + "Fizz"
    if num % 3 == 0:
        string = string + "Buzz"
    if num % 5 == 0:
        string = string + "Bazz"
    print string
    string = ""
    
