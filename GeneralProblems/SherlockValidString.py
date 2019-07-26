from collections import Counter

def isValid(s):
    s = Counter(s)
    s = sorted(s.values())
    l = len(s)

    if (s.count(s[0]) == l) or (s.count(s[0]) == l-1 and s[-1]-s[-2] == 1) or (s.count(s[-1]) == l-1 and s[0] == 1):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    
    s = input()

    result = isValid(s)

    print(result)
