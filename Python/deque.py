# deque - a double-ended queue that is mutable and be assigned via index
#  is much faster to insert an item at the start of it than it is as the start of a list
from collections import deque

dq = deque('abcde')
print(dq) # deque(['a','b','c','d','e']

# insert item on the right side of the queue
dq = deque('abcde')
dq.append('10')

# insert item on the left side of the queue
x = deque('123456789')
x.appendleft('10')
print(x)

# insert multiple items on the left side of the queue
x = deque('12345') # deque(['a', 'b', 'c', 'd', 'e'])
x.extendleft('abcd') # deque(['10', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
print(x) # deque(['d', 'c', 'b', 'a', '1', '2', '3', '4', '5'])
