'''normal approach of tranversing the string from the opposite order and appending it to the new string this results in a new string which is reversal of the old one'''

def simple_reverse(string):
    new_string = []
    for i in range(len(string) - 1 , -1 , -1):
        new_string.append(string[i])
    return ''.join(new_string)


string = 'tanmay'
print(simple_reverse(string))



'''swap the first and the last elements of the string till half of the string to get a fully reversed string saves the space complexity from the previous step of having an extra string'''

def swap(string , a, b):
    string = list(string)
    temp =  string[a]
    string[a] = string[b]
    string[b] = temp
    return''.join(string)

def smart_reverse(string):
    for i in range(len(string)//2):
        string = swap(string , i , len(string)-i-1)
    return string

print(smart_reverse(string))

#built in functions

#Apart from these, some built-in functions that can be used to reverse a string are as follows:

string1 = 'abcde'
string2 = reversed(string1)
print(''.join(string2))

list1 = list(string1)
list1.reverse()
print(''.join(list1))

#Both these methods are of O(n) time complexity
