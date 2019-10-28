# Given a function  f(x, y) and a value z, return all positive integer pairs x and y where f(x, y) == z.

# The function is constantly increasing, i.e.:

# f(x, y) < f(x + 1, y)
# f(x, y) < f(x, y + 1)


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        r = []
        for i in range(1, 1001):
            if customfunction.f(i, 1) <= z and customfunction.f(i, 1000) >= z:
                for j in range(1, 1001):
                    if customfunction.f(i, j) == z:
                        r.append([i, j])
                        break
        return r
