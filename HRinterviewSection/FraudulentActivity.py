# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. 
# If the amount spent by a client on a particular day is greater than or equal to 2 X the client's median spending 
# for a trailing number of days, they send the client a notification about potential fraud. 
# The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
from bisect import insort, bisect_left

d = int(input())
exp = list(map(int, input().strip().split()))

def activityNotification(d, expenditure):
    v = sorted(expenditure[: d])
    count = 0
    for i, current in enumerate(expenditure[d:]):
        de = expenditure[i]
        if d % 2 == 0:
            if current >= v[d//2] + v[d//2-1]:
                count += 1
        elif current >= v[d//2]*2:
                count += 1
        ix = bisect_left(v, de)
        del v[ix]
        insort(v, current)
    return count

result = activityNotification(d, exp)
print(result)
