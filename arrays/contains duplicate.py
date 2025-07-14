#O(n^2)
def brute_force_duplicate(array):
    for i in range(len(array)-1):
        for j in range (i+1 , len(array)):
            if array[i] == array[j] :
                return True 
            return False
        
array = []
print(brute_force_duplicate(array))

#O(nlogn) sort and search 
def better_duplicate_search(array):
    array.sort()
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            return True 
    return False

print(better_duplicate_search(array))

#hash map ez O(n)
def smart_duplicate_search(array):
    dictionary = dict()
    if len(array)<2:
        return False
    else:
        for i in range(len(array)):
            if array[i] in dictionary:
                return True
            else:
                dictionary[array[i]] = True
    return False

print(smart_duplicate_search(array))

        