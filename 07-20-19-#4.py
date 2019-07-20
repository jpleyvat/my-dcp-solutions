
# Given an array of integers, find the first missing 
# positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that 
# does not exist in the array. The array can contain 
# duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. 
# The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


def missing(data, n, positive_missing):
    index = (len(data) - 1) - n
    if(n>=0):
        if not ((data[index] + 1) in data):
            if((data[index] + 1) > 0):
                positive_missing.append(data[index] + 1)
        missing(data, n - 1, positive_missing)
    return min(positive_missing)
            
def caller(data):
    n = len(data)
    positive_missing = []
    return missing(data, n - 1, positive_missing)

data = [-1,-2,-10,1,2, -5, 4]

print(caller(data))