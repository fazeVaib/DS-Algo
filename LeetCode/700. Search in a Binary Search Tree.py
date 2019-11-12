# 700. Search in a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while True:
            if root.val == val:
                return root
            elif root.val < val and root.right != None:
                root = root.right
            elif root.val > val and root.left != None:
                root = root.left
            else:
                return None
        return None
