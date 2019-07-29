# A group of friends want to buy a bouquet of flowers. 
# The florist wants to maximize his number of new customers and the money he makes.
# To do this, he decides he'll multiply the price of each flower by the number of 
# that customer's previously purchased flowers plus 1

def getMinCost(k, c):
    counter = [0]*k
    totalcost = 0
    arr = sorted(c, reverse=True)
    for i in range(len(arr)):
        totalcost += (i//k + 1)*arr[i]
    return totalcost


if __name__ == "__main__":
    k = int(input())
    c = list(map(int, input().strip().split()))

    r = getMinCost(k, c)
    print(r)
