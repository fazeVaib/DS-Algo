# 461. Hamming Distance


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        return sum([i == '1' for i in bin(x ^ y)])
