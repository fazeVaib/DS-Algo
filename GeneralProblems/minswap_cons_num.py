arr = list(map(int, input().strip().split()))

def minswap(arr):
    first = 0
    last = len(arr) - 1
    swap = 0

    while first < last:
        while arr[first] == first+1:
            first += 1
            if first >= last:
                break

        else:
            temp = arr[arr[first]-1]
            arr[arr[first]-1] = arr[first]
            arr[first] = temp
            swap += 1
            print("Array now: ", arr)
    return swap

print("Num of swaps: ", minswap(arr))
    