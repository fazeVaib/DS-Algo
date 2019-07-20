# Complete the countTriplets function in the editor below.
# It should return the number of triplets forming a geometric progression for a given r as an integer.

from collections import Counter, defaultdict

r = int(input())
seq = list(map(int, input().strip().split()))

def countTriplet(seq, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in seq:
        print("k= ", k)
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
        print('new v3: ', v3)
        print('new v2:', v2)
        print(count)
        print('---------------------------')

    return count

print(countTriplet(seq, r))
