'''stack means last in first out 
only concerned whats at the top
peek means just to see whats at the top  
stacks append and pop on the right'''

''' queues are FIFO that is first in first out'
queues append on the right and pop from the left  '''

# Stacks - Last in First Out (Lifo)

stk = []

# Append to top of stack - O(1)
stk.append(5)

stk.append(4)
stk.append(3)

print(stk)

# Pop from stack - O(1)
x = stk.pop()

# Ask what's on the top of stack - O(1)
print(stk[-1])

# Ask if something is in the stack - O(1)
if stk:
  print(True)

# Queues - First in First out (Fifo)

from collections import deque

q = deque()

# Enqueue - Add element to the right - O(1)
q.append(5)
q.append(6)
q.append(7)
print(q)

# Deqeue (pop left) - Remove element from the left - O(1)
q.popleft()

print(q)

# Peek from left side - O(1)
print(q[0])

# Peek from right side - O(1)
print(q[-1])