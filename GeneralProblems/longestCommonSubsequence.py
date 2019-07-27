# A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. 
# Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?
# For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. 
# They can be formed by eliminating either the D or C from both strings. 
# Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD not equal ABDC.

def commonChild(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    grid = [[0 for x in range(l1 + 1)] for y in range(l2 + 1)]
    for i in range(1, l2 + 1):
        for j in range(1, l1 + 1):
            if s2[i-1] == s1[j-1]:
                grid[i][j] = grid[i-1][j-1] + 1
            else:
                grid[i][j] = max(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]



if __name__ == "__main__":
    s1 = input()
    s2 = input()
    result = commonChild(s1,s2)
    print(result)

