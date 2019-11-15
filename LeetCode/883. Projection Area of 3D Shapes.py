# 883. Projection Area of 3D Shapes
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xnum = len(grid)
        ynum = len(grid[0])
        xy = 0
        yz = 0
        xz = [0]*ynum
        # print(grid[0][0])

        for i in range(xnum):
            yz += max(grid[i])
            for j in range(ynum):
                # print(i, j)
                if grid[i][j] != 0:
                    xy += 1
                if grid[i][j] > xz[j]:
                    xz[j] = grid[i][j]

        return xy + yz + sum(xz)
