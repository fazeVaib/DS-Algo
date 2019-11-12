# 942. DI String Match


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l = len(S)
        s = 0
        if S[0] == 'I':
            lst = [s]
            s += 1
        else:
            lst = [l]
            l -= 1

        for i in range(1, len(S)):
            if S[i] == 'I':
                lst.append(s)
                s += 1
            else:
                lst.append(l)
                l -= 1

        lst.append(s)
        return lst
