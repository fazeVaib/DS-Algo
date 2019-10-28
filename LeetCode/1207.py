# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for item in arr:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1

        s = list(d.values())
        if len(s) == len(set(s)):
            return True
        else:
            return False
