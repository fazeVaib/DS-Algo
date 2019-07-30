def whatFlavour(cost, money):
    m = {}
    for pos, value in enumerate(cost):
        if money-value not in m:
            m[value] = pos+1
        else:
            print(pos+1 , " ", m[money-value])


if __name__ == "__main__":
    money = int(input())
    cost = list(map(int, input().strip().split()))
    whatFlavour(cost, money)