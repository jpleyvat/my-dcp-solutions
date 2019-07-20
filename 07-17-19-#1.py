
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def checker(data, k, n, summands):
    if(n<=0):
        print("False")
    else:
        if(data[len(data) - n] in summands):
            print("True")
        else:
            summands[len(data) - n] = (k -data[len(data) - n])

            checker(data, k, n - 1, summands)
        
def caller(data, k):
    summands = [None] * len(data)
    checker(data, k, len(data), summands)

data = [1,1,1,1,1,1,1,1,1,1, 100, 99]
k = 100

caller(data, k)
