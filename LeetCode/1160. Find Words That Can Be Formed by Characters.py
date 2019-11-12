# 1160. Find Words That Can Be Formed by Characters

from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        f = 0
        reflist = Counter(chars)
        for ele in words:
            elet = Counter(ele)
            curr = True
            for i in elet:
                if i not in reflist:
                    curr = False
                    break
                elif reflist[i] < elet[i]:
                    curr = False
                    break

            if curr == True:
                f += len(ele)

        return f
