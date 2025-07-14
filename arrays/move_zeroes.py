"""approach 1 : for each zero popped append it at the end of the array"""

def native_zero_mover(array):
    l = len(array)
    for i in range(l):
        if array[i] == 0 :
            array.append(0)

    j = 0
    c = 0
    while c < l :
        if array[j] != 0 : 
            j += 1 
        else : 
            array.pop(j)
        c += 1 
    return array 

array = []
print(native_zero_mover(array))


"""approach 2 : for every zero that you meet traverse the list and swap it with the immediate non zero element"""

def swap_move(array):
    z = 0 
    for i in range(len(array)):
        if array[i] != 0 :
            array[i] , array[z] = array[z] , array[i]
            z += 1 
        return array 
print(swap_move(array))

"""approach 3 : one liner : we know that all the values apart from zero are marked as 1 in boolean and 0 is marked as 0 in boolean , 
therefore we sort the array based on the boolea therefore we sort it based decending values so all the zeroes come at last """

def one_liner (array):
    array.sort(key = bool , reverse = True)
    return array 
print(one_liner(array))

