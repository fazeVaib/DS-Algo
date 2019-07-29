# A string is said to be a special string if either of two conditions is met:
# All of the characters are the same, e.g. aaa.
# All characters except the middle one are the same, e.g. aadaa.
# A special substring is any substring of a string which meets one of those criteria. 
# Given a string, determine how many special substrings can be formed from it.
# For example, given the string, we have the following special substrings:


def subStrCount(n, s):
    l=[]
    count = 0
    curr = None

    for i in range(n):
        if s[i] == curr:
            count += 1
        else:
            if curr is not None:
                l.append((curr,count))
            curr = s[i]
            count = 1
    l.append((curr, count))

    result = 0

    for item in l:
        result += (item[1] * (item[1]+1))//2

    for i in range(1, len(l)-1):
        if l[i-1][0] == l[i+1][0] and l[i][1]==1:
            result += min(l[i-1][1], l[i+1][1])

    return result



if __name__ == "__main__":
    n = int(input())
    s = input()
    result = subStrCount(n, s)
    print(result)