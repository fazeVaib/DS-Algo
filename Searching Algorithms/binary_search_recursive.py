def binarySearchRecursive(a, l, r, x):
    if l <= r:
        m = int(l + (r-l)/2)
        # If the element is present at the middle itself
        if a[m] == x:
            return m
        # If element is smaller than middle element, then it can only be present in left sub-array
        elif x > a[m]:
            return binarySearchRecursive(a, m+1, r, x)
        # If element is greater than middle element, then it can only be present in right sub-array
        else:
            return binarySearchRecursive(a, l, m-1, x)
    return -1


a = list(map(int, input("Enter a list of elements: ").split()))
x = int(input("Enter the element to be searched: "))
r = binarySearchRecursive(a, 0, len(a)-1, x)
if r != -1:
    print("Entered element", x, "found at position:", r+1)
else:
    print("Entered element is not found in array")

