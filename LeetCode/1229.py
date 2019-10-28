class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        i, j = 0, 0

        while i < len(slots1) and j < len(slots2):
            if slots1[i][1] < slots2[j][0]:
                i += 1
            elif slots2[j][1] < slots1[i][0]:
                j += 1
            else:
                s = max(slots1[i][0], slots2[j][0])
                e = min(slots1[i][1], slots2[j][1])

                if e-s >= duration:
                    return [s, s + duration]

                if slots1[i][1] > slots2[j][1]:
                    j += 1
                else:
                    i += 1

        return []
