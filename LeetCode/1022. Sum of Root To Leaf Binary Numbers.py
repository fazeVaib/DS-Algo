# 1022. Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    sum = 0
    
    def sumRoot(self, root: TreeNode, p):
        if not root:
            return None
        
        p += str(root.val)
        
        if root.left == None and root.right == None:
            self.sum += int(p,2)
        
        self.sumRoot(root.left, p) 
        self.sumRoot(root.right, p)
        return None
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.sumRoot(root, '')
        return self.sum