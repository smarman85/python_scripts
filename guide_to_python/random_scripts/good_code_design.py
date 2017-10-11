# #Bad
# # creates a concatenated string from 0 to 10 
# nums = ""
# for n in range(20):
#     nums += str(n) # slow and inefficient
# print nums

# good:
nums = map(str, range(20))
#print(list(nums)) # output: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
print("".join(nums)) # more efficient # output: 012345678910111213141516171819
