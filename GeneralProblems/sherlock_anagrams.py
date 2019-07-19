# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
def sherlock_anagrams(s):
    s = list(s)
    l = len(s)
    count = 0
    for i in range(l-1):
        for j in range(i+1,l):
            for k in range(1, l-j+1):
                if sorted(s[i:i+k]) == sorted(s[j:j+k]):
                    count += 1
    return count

n = int(input())
for _ in range(n):
    s  = input()
    r = sherlock_anagrams(s)
    print(r)
