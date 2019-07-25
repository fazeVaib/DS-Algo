# In an array, , the elements at indices  and  (where ) form an inversion if . 
# In other words, inverted elements  and  are considered to be "out of order".
# To correct an inversion, we can swap adjacent elements.
# For example, consider the dataset . It has two inversions: and . 
# To sort the array, we must perform the following two swaps to correct the inversions:
# Given  datasets, print the number of inversions that must be swapped to sort each dataset on a new lin

def sort(arr):
    l = len(arr)
    mid = l//2
    if l >= 2:
        sortedLeft, countLeft = sort(arr[:mid])
        sortedRight, countRight = sort(arr[mid:])
        result, counts = merge(sortedLeft, sortedRight)
        return result, counts + countLeft + countRight
    else:
        return arr, 0 

def merge(sortedLeft, sortedRight):
    inversions = 0
    result = []
    leftMark = 0
    rightMark = 0
    lLeft = len(sortedLeft)
    lRight = len(sortedRight)

    while lLeft > leftMark and lRight > rightMark:
        if sortedLeft[leftMark] <= sortedRight[rightMark]:
            result.append(sortedLeft[leftMark])
            leftMark += 1
        else:
            inversions += lLeft - leftMark
            result.append(sortedRight[rightMark])
            rightMark += 1

    if lLeft == leftMark:
        result += sortedRight[rightMark:]
    elif lRight == rightMark:
        result += sortedLeft[leftMark:]

    return result, inversions


def countInversions(arr):
    finalArray, inversions = sort(arr)
    return inversions


d = int(input())
for _ in range(d):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(countInversions(arr))
