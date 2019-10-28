# Missing number in arithmetic progression


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr) + 1
        return int((n*(arr[0] + arr[-1])/2) - (sum(arr)))
