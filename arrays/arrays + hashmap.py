'''
arrays are mutable i.e. changeable in terms of sizes and elements 
deletion and insertion are in O(n)
'''

'''
dynamic arrays in python are called lists 
strings are immutable 
'''

A = [1, 2, 3]

print(A)

# Append - Insert element at end of array - On average: O(1)
A.append(5)

print(A)

# Pop - Deleting element at end of array - O(1)
A.pop()

print(A)

# Insert (not at end of array) - O(n)
A.insert(2, 5)

print(A)

# Modify an element - O(1)
A[0] = 7

print(A)

# Accessing element given index i - O(1)
print(A[2])


# Checking if array has an element - O(n)
if 7 in A:
  print(True)

  # Checking if array has an element - O(n)
if 7 in A:
  print(True)

  # Append to end of string - O(n)
s = 'hello'

b = s + 'z'

print(b)

# Append to end of string - O(n)
s = 'hello'

b = s + 'z'

print(b)

# Access positions - O(1)
print(s[2])

# Check length of string - O(1)
len(s)



'''Hash tables and Hash Map'''

s = set()
print(s)

s.add(1)
s.add(2)
s.add(3)

print(s)

if 1 not in s :
  print(True)

s.remove(3)

print(s)


string = 'aaaaaaaaaaaannnnnnnnnnnndddddddddd'

sett = set(string)

print(sett)

for x in s : 
  print(x)


'''Hash maps in python are called dictionaries '''

d = {'greg': 1, 'steve': 2, 'rob': 3}

print(d)

d['arsh'] = 4 
print(d)

if 'greg' in d :
  print(True)

# Check the value corresponding to a key in the dictionary: O(1)
print(d['greg'])

#loop over key value pairs of the dictionary

for key , val in d.items():
  print(f'key {key}:val {val}')

#Defaultdict


from collections import defaultdict

default = defaultdict(list)

default[2] 

print(default)


# Counter
from collections import Counter

counter = Counter(string)

print(counter)