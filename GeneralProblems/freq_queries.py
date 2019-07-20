# You are given  queries. Each query is of the form two integers described below:
# 1 x-: Insert x in your data structure.
# 2 y-: Delete one occurence of y from your data structure, if present.
# 3 z-: Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

from collections import defaultdict

n = int(input())
q = []

for _ in range(n):
    q.append(list(map(int, input().strip().split())))

def freqQuery(queries):
    count = defaultdict(int)
    freq = defaultdict(int)
    result = []

    for query in queries:
        if query[0] == 1:
            count[freq[query[1]]] -= 1
            freq[query[1]] += 1
            count[freq[query[1]]] += 1

        elif query[0] == 2:
            if freq[query[1]] > 0:
                count[freq[query[1]]] -= 1
                freq[query[1]] -= 1
                count[freq[query[1]]] += 1

        else:
            if count[query[1]] > 0:
                result.append(1)
            else:
                result.append(0)

    return result

print(freqQuery(q))




