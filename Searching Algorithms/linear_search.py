def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            print("Element", x, "found at position: ", i+1)
            break
    else:
        print("Entered element is not found in the given list")


a = list(map(int, input("Enter a list of elements: ").split()))
x = int(input("Enter the element to be searched: "))
linear_search(a, x)

