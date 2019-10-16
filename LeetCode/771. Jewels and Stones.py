class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = list(J)
        count = 0
        dict = {}
        for item in J:
            dict[item] = 0
            
        for items in S:
            try:
                if dict[items] == 0:
                    count += 1
            except Exception:
                pass
        return count