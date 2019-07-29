# Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

# For example, the length of your array of zeros n=10 . Your list of queries is as follows:

#     a b k
#     1 5 3
#     4 8 7
#     6 9 1
# Add the values of k  between the indices a and b inclusive:

# index -> 1 2 3  4  5 6 7 8 9 10
# 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 	[3, 3, 3, 3, 3, 0, 0, 0, 0, 0]
# 	[3, 3, 3, 10, 10, 7, 7, 7, 0, 0]
# 	[3, 3, 3, 10, 10, 8, 8, 8, 1, 0]
# The largest value is 10 after all operations are performed.

nm = input().split()
n = int(nm[0])
m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().strip().split())))

# O(n*m) time complexity, so quite expensive
# def arrayManip(n, queries):
#     finalarray = [0]*n
#     for q in queries:
#         for i in range(q[0]-1, q[1]):
#             finalarray[i] += q[2]

#     return max(finalarray)

def arrayManip(n, queries):  # O(n) time complexity. Used Prefix sum technique 
    f = [0]*(n+1)
    for q in queries:
        f[q[0]-1] += q[2]
        if q[1]<=(n): f[q[1]] -= q[2]
    maxnum = x = 0
    for i in f:
        x = x+i 
        if x>maxnum: maxnum=x
    return maxnum


r = arrayManip(n, queries)
print("Result is: ", r)