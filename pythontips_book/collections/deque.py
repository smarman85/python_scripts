from collections import deque
# now instantiate the deque object
d = deque()

#it works like python lists and provides you with somewhat similar methods as well
d.append('1')
d.append('2')
d.append('3')

print len(d)
# Output: 3

print d[0]
# Output: '1'

print d[-1]
# Output: '3'

# you can pop values from both sides o the deque
d = deque(range(5))
print len(d)
# output: 5

d.popleft()
# output: 0

d.pop()
# output: 4

print d


# can also limit the ammount of items  deque can hold.# do this we achieve the max limit of our deque it will pop out items from the oppsite end
d = deque(maxlen=30)

d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print d
