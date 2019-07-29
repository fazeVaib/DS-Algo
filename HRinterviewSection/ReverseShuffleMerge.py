# https://www.hackerrank.com/challenges/reverse-shuffle-merge/

from collections import Counter

def reverseShuffleMerge(s):
    cur = Counter(s)
    std = {char: cur[char] / 2 for char in cur}
    stack = []
    for i in s[::-1]:
        cur[i] -= 1
        if std[i]:
            std[i] -= 1
            while stack:
                std[stack[-1]] += 1
                if i < stack[-1] and all(std[i] <= cur[i] for i in std):
                    stack.pop()
                else:
                    std[stack[-1]] -= 1
                    break
            stack.append(i)
    return ''.join(stack)
    # totalCount = Counter(s)
    # originalCount = {}
    # for item in totalCount:
    #     originalCount[item] = totalCount[item]//2
    # order = sorted(totalCount.keys())
    # result = []

    # for i in range(len(s)-1, -1, -1):
    #     print("TotalCount: ", totalCount)
    #     print("OriginalCOunt: ", originalCount)
    #     print("Order = ", order)
    #     print("Result before {0} is {1}".format(s[i], result))
    #     if s[i] == order[0]:
    #         result.append(s[i])
    #         originalCount[s[i]] -= 1
    #     else:
    #         if totalCount[s[i]] == originalCount[s[i]]:
    #             result.append(s[i])
    #             originalCount[s[i]] -= 1
    #     totalCount[s[i]] -= 1

    #     if originalCount[s[i]] == 0:
    #         order.remove(s[i])
    #         originalCount[s[i]] -= 1
    #     if len(order)<1:
    #         return ''.join(result)

    # return ''.join(result)
            


if __name__ == "__main__":
    s = input()
    r = reverseShuffleMerge(s)
    print(r)
