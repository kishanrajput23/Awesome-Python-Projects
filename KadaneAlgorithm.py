def maxSubArraySum(arr,size):
    
    max_till_now = arr[0]
    max_ending = 0
    
    for i in range(0, size):
        max_ending = max_ending + arr[i]
        if max_ending < 0:
            max_ending = 0
        
        
        elif (max_till_now < max_ending):
            max_till_now = max_ending
            
    return max_till_now

arr = [-2, -3, 4, -1, -2, 5, -3]
print("Maximum Sub Array Sum Is" , maxSubArraySum(arr,len(arr)))


"""Output
The output of the above code will be as given below:

Maximum Sub Array Sum Is 6

Time Complexity
The time complexity of kadane’s algorithm for an array containing n integer element is O(n) as only one for loop is to be executed throughout the program. Similarly, the auxiliary space complexity of the algorithm is O(1).
"""