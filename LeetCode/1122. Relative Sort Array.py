# 1122. Relative Sort Array

from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        f = []
        for ele in arr2:
            f += [ele]*c[ele]

        for ele in sorted(list(set(arr1) - set(arr2))):
            f += [ele]*c[ele]

        return f
