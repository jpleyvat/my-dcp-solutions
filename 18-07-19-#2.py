# such that each element at index i of the new array 
# is the product of all the numbers in the original 
# array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would 
# be [2, 3, 6].

# Follow-up: what if you can't use division?

def multiplier(data, n, actual_index, multiplication):
    if(n<0):
        return multiplication
    if(((index) - n) != actual_index):
        multiplication = multiplication * data[(index) - n]
    return multiplier(data, n-1, actual_index, multiplication)


    
def sorter(data, n, actual_index, result):
    
    actual_index = (index) - n
    multiplication = 1
    if(n >= 0):
        result[(index) - n] = multiplier(data, index, actual_index, multiplication)
        sorter(data, n-1, actual_index, result)

def caller(data):
    n = index
    actual_index = 0
    result = [None] * len(data)
    sorter(data, n , actual_index, result)
    print(result)

data = [1,2,3,4,5]

index = len(data) - 1
caller(data)
