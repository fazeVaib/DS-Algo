class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        bal = 0
        for i in s:
            if i == 'L':
                bal -= 1
            else:
                bal += 1

            if bal == 0:
                count += 1

        return count
