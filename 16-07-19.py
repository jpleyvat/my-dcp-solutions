# Write a program that shows how many ways are 
# there to decode a message if a=1, b=2, c=3... z=26

def num_recursive(data, n, memo):
    if(n <= 0):
        return 1
    elif(data[len(data) - n] == '0'):
        return 0
    elif(memo[n] != None):
        return memo[n]
    result = num_recursive(data, n - 1, memo)
    if(n >= 2 and int(data[len(data) - n] + data[len(data) - n + 1]) <= 26):
        result += num_recursive(data, n - 2, memo)

    memo[n] = result
    return result

def num_ways(data):
    n = len(data)
    memo = [None] * (n + 1)
    return num_recursive(data, n , memo)

data = input("Write a secret code: ")

print(num_ways(data))