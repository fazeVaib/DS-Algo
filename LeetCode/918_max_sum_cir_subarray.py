def maxSubarraySumCircular(A) -> int:
        
    if len(A) == 1:
        return A[0]
        
    curr_max = global_max = A[0]
    for i in range(1, len(A)):
        curr_max = max(A[i], curr_max + A[i])
        global_max = max(curr_max, global_max)
        
    cm = gm = A[0]
    for i in range(1, len(A)):
        cm = min(A[i], cm + A[i])
        gm = min(cm, gm)
    
    if global_max < 0 or gm > 0:
        return global_max
    
    return max(global_max, sum(A) - gm)

print(maxSubarraySumCircular([5,-3,5]))