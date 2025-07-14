def brute_force_max_subarray(array):
    maximum = 0
    if len(array) == 0 :
        return None
    for i in range (len(array)):
        cum_sum = 0 
        for j in range (i , len(array)):
            cum_sum += array(j)
            maximum = max(maximum , cum_sum)
        return maximum 

    array = []
    print(brute_force_max_subarray(array))

#What's happening here is each iteration of the outer loop is giving us all the possible subarrays starting from the ith index.
#For example, in the first iteration we get all the subarrays starting with the first element and so on.
#Now with the second for loop we are building a subarray starting from the ith index to the last index
#In the process we are cumulating the sum at every iteration which is giving us the sum of the subarray from the ith index to the jth index
#Then we are checking if the cumulative sum is greater than all other cumulative sums we have found so far and storing the greatest sum in "maximum"
#Finally we return maximum which contains the greatest sum of any subarray in the array.
#Since we are looping through two nested for loops the time complexity is O(n^2)


#Kadanes algo 

def kadane(array):
    maximum = maxarray = array[0]
    for i in range (1 , len(array)):
        maxarray =  max(array[i] , maxarray + array[i])
        maximum = max(maxarray , maximum )
    return maximum

    print(kadane(array))