my_list = [i ** 2 for i in range(1, 11)]

my_file = open("outtest.txt", "w")

# Add your code below!
for num in my_list:
  my_file.write(str(num) + "\n")

my_file.close()
