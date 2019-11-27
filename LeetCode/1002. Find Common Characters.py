# 1002. Find Common Characters

from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        f = Counter(A[0])
        for a in A:
            f &= Counter(a)
            
        return [ ele for ele in f.elements()]